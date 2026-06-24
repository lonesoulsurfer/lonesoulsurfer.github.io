#!/usr/bin/env python3
"""
download_archive.py  --  Download all Instructables content to local markdown + images

Usage:
    python3 download_archive.py                    # archive everything
    python3 download_archive.py --new-only         # only projects not yet archived
    python3 download_archive.py --url <URL>        # archive one specific project

Output structure:
    ../archive/instructables/
    ├── led-filament-lamp/
    │   ├── index.md        ← all steps as clean markdown
    │   └── images/
    │       ├── step1_01.jpg
    │       ├── step2_01.jpg
    │       └── ...
    ├── simple-fire-piston/
    │   ├── index.md
    │   └── images/
    ...

Requirements:
    pip install requests beautifulsoup4 markdownify

Notes:
    - Full archive of 254 projects with all images will be 2-5 GB and take 1-2 hours.
    - Run with --new-only after each new Instructable to keep archive current.
    - Images are saved with descriptive names so they're readable offline.
    - Git LFS is required for the images folder. See README for setup.
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Missing dependencies. Run:  pip install requests beautifulsoup4 markdownify")
    sys.exit(1)

try:
    from markdownify import markdownify as md
    HAS_MARKDOWNIFY = True
except ImportError:
    HAS_MARKDOWNIFY = False
    print("[warn] markdownify not installed -- steps will be saved as plain text")
    print("       Run:  pip install markdownify")

# ── CONFIG ───────────────────────────────────────────────────────────────────
BASE_URL     = "https://www.instructables.com"
PROJECTS_JSON = Path(__file__).parent.parent / "projects.json"
ARCHIVE_DIR  = Path(__file__).parent.parent / "archive" / "instructables"
DELAY        = 1.2   # seconds between requests (archive runs slowly -- be respectful)
IMG_DELAY    = 0.3   # between image downloads
MAX_IMG_SIZE = 20 * 1024 * 1024  # skip images over 20MB

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept":          "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer":         BASE_URL,
}


# ── HELPERS ──────────────────────────────────────────────────────────────────

def get(url, session, stream=False, retries=3):
    for attempt in range(retries):
        try:
            time.sleep(DELAY if not stream else IMG_DELAY)
            r = session.get(url, headers=HEADERS, timeout=30, stream=stream)
            r.raise_for_status()
            return r
        except requests.RequestException as e:
            print(f"    [warn] attempt {attempt+1} failed: {e}")
            time.sleep(2 ** attempt)
    return None


def slugify(text):
    """Convert a title to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:80]


def slug_from_url(url):
    """Extract slug from an Instructables URL."""
    path = urlparse(url).path.strip("/")
    return path.split("/")[-1] if path else slugify(url)


def safe_filename(name, ext=""):
    """Make a safe filename."""
    name = re.sub(r'[<>:"/\\|?*]', "_", name)
    name = name.strip(". ")[:100]
    return name + ext


def download_image(img_url, dest_path, session):
    """Download one image. Returns True on success."""
    if dest_path.exists():
        return True  # already downloaded

    r = get(img_url, session, stream=True)
    if not r:
        return False

    # Check content length before downloading
    content_length = int(r.headers.get("content-length", 0))
    if content_length > MAX_IMG_SIZE:
        print(f"    [skip] image too large ({content_length//1024}KB): {img_url}")
        return False

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except IOError as e:
        print(f"    [error] could not save {dest_path}: {e}")
        return False


# ── PARSING ──────────────────────────────────────────────────────────────────

def extract_img_ext(url):
    """Get file extension from image URL."""
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
        ext = ".jpg"
    return ext


def parse_instructable(html, page_url, images_dir, session):
    """
    Parse a full Instructable page.
    Returns (markdown_string, list_of_downloaded_image_paths)
    """
    soup = BeautifulSoup(html, "html.parser")
    lines = []
    downloaded_images = []

    # ── Title ──
    title_el = soup.find("h1") or soup.find("title")
    title = title_el.get_text(strip=True) if title_el else "Untitled"
    lines.append(f"# {title}\n")
    lines.append(f"Source: {page_url}\n")

    # ── Author / date ──
    author_el = soup.select_one("span.author, a.author, [itemprop='author']")
    date_el   = soup.select_one("time, span.date, [itemprop='datePublished']")
    meta_parts = []
    if author_el:
        meta_parts.append(f"By: {author_el.get_text(strip=True)}")
    if date_el:
        meta_parts.append(f"Published: {date_el.get('datetime', date_el.get_text(strip=True))}")
    if meta_parts:
        lines.append("  ".join(meta_parts) + "\n")

    lines.append("---\n")

    # ── Cover image ──
    og_img = soup.find("meta", property="og:image")
    if og_img and og_img.get("content"):
        cover_url = og_img["content"]
        ext = extract_img_ext(cover_url)
        fname = f"cover{ext}"
        dest = images_dir / fname
        if download_image(cover_url, dest, session):
            lines.append(f"![Cover](images/{fname})\n")
            downloaded_images.append(dest)

    # ── Steps ──
    # Instructables uses section.step or div.step
    steps = soup.select("section.step, div.step, article.step")

    if not steps:
        # Fallback: look for step headers
        steps = soup.select("div[id^='step'], section[id^='step']")

    if not steps:
        # Last resort: just grab all body content
        body = soup.select_one("div#content, main, article, div.instructable-content")
        if body:
            steps = [body]

    for step_idx, step in enumerate(steps, 1):
        # Step title
        step_title_el = step.find(re.compile(r"^h[1-6]$"))
        step_title = step_title_el.get_text(strip=True) if step_title_el else f"Step {step_idx}"
        lines.append(f"\n## {step_title}\n")

        # Step images
        step_imgs = step.find_all("img", src=True)
        for img_idx, img_el in enumerate(step_imgs, 1):
            src = img_el.get("src", "")
            if not src or "pixel.png" in src or "assets" in src:
                continue
            if src.startswith("//"):
                src = "https:" + src
            elif src.startswith("/"):
                src = urljoin(BASE_URL, src)

            ext = extract_img_ext(src)
            fname = f"step{step_idx:02d}_{img_idx:02d}{ext}"
            dest = images_dir / fname
            if download_image(src, dest, session):
                alt = img_el.get("alt", f"Step {step_idx} image {img_idx}")
                lines.append(f"![{alt}](images/{fname})\n")
                downloaded_images.append(dest)

        # Step text
        # Remove img tags from a copy so we don't double-process
        step_copy = BeautifulSoup(str(step), "html.parser")
        for img in step_copy.find_all("img"):
            img.decompose()
        for nav in step_copy.find_all(["nav", "footer", "aside"]):
            nav.decompose()
        # Remove the title we already added
        for h in step_copy.find_all(re.compile(r"^h[1-6]$")):
            h.decompose()

        if HAS_MARKDOWNIFY:
            step_md = md(str(step_copy), heading_style="ATX", bullets="-").strip()
        else:
            step_md = step_copy.get_text("\n", strip=True)

        if step_md:
            lines.append(step_md + "\n")

    return "\n".join(lines), downloaded_images


# ── ARCHIVE ONE PROJECT ───────────────────────────────────────────────────────

def archive_project(project_url, project_title, session):
    """
    Download one Instructable to the archive folder.
    Returns True on success.
    """
    folder_name = slug_from_url(project_url)
    project_dir = ARCHIVE_DIR / folder_name
    index_path  = project_dir / "index.md"
    images_dir  = project_dir / "images"

    # Skip if already fully archived
    if index_path.exists() and images_dir.exists():
        print(f"  [skip] already archived: {folder_name}")
        return True

    print(f"  Archiving: {project_title[:60]}")
    r = get(project_url, session)
    if not r:
        print(f"  [error] could not fetch {project_url}")
        return False

    project_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    markdown, imgs = parse_instructable(r.text, project_url, images_dir, session)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"    Saved: {index_path.name} + {len(imgs)} images")
    return True


# ── INDEX PAGE ────────────────────────────────────────────────────────────────

def write_archive_index(projects):
    """Write a simple markdown index of all archived projects."""
    index_path = ARCHIVE_DIR.parent / "README.md"
    lines = [
        "# lonesoulsurfer -- Instructables Archive\n",
        f"Local backup of {len(projects)} Instructables by lonesoulsurfer.\n",
        "Each folder contains `index.md` (all steps as markdown) and `images/`.\n",
        "\n---\n",
    ]

    # Group by category
    from collections import defaultdict
    by_cat = defaultdict(list)
    for p in projects:
        by_cat[p.get("category", "making")].append(p)

    for cat in sorted(by_cat):
        lines.append(f"\n## {cat.title()}\n")
        for p in by_cat[cat]:
            folder = slug_from_url(p["url"])
            title  = p["title"]
            views  = p.get("views", 0)
            view_str = f"{views:,}" if views else "--"
            lines.append(f"- [{title}](instructables/{folder}/index.md) ({view_str} views)\n")

    with open(index_path, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Wrote archive index: {index_path}")


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Archive Instructables locally")
    parser.add_argument("--new-only", action="store_true",
                        help="Only archive projects not yet in the archive folder")
    parser.add_argument("--url", type=str,
                        help="Archive a single specific Instructable URL")
    args = parser.parse_args()

    print("=" * 60)
    print("lonesoulsurfer Instructables archive downloader")
    print("=" * 60)

    session = requests.Session()

    # Single URL mode
    if args.url:
        title = args.url.split("/")[-2].replace("-", " ").title()
        archive_project(args.url.rstrip("/") + "/", title, session)
        return

    # Load project list from projects.json
    if not PROJECTS_JSON.exists():
        print(f"ERROR: {PROJECTS_JSON} not found.")
        print("Run scrape.py first to generate the project list.")
        sys.exit(1)

    with open(PROJECTS_JSON) as f:
        projects = json.load(f)

    print(f"Loaded {len(projects)} projects from {PROJECTS_JSON.name}")

    if args.new_only:
        before = len(projects)
        projects = [p for p in projects
                    if not (ARCHIVE_DIR / slug_from_url(p["url"]) / "index.md").exists()]
        print(f"  {before - len(projects)} already archived, {len(projects)} to download")

    if not projects:
        print("Nothing to archive.")
        return

    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    success = 0
    fail    = 0
    for i, p in enumerate(projects, 1):
        print(f"\n[{i}/{len(projects)}]")
        ok = archive_project(p["url"], p["title"], session)
        if ok:
            success += 1
        else:
            fail += 1

    # Reload full list for index (not just the ones we just downloaded)
    with open(PROJECTS_JSON) as f:
        all_projects = json.load(f)
    write_archive_index(all_projects)

    print(f"\n{'='*60}")
    print(f"Done. {success} archived, {fail} failed.")
    print(f"Archive location: {ARCHIVE_DIR}")
    print("\nRemember to commit with Git LFS enabled:")
    print("  git lfs track 'archive/**/*.jpg'")
    print("  git lfs track 'archive/**/*.png'")
    print("  git add .gitattributes archive/")
    print("  git commit -m 'update archive'")
    print("  git push")


if __name__ == "__main__":
    main()
