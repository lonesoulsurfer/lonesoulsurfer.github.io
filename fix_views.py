"""
Adds view count extraction to download_archive.py using Playwright,
and updates projects.json with the correct counts.

Run from repo root: python fix_views.py
"""
from pathlib import Path
import re

path = Path("scraper/download_archive.py")
content = path.read_text(encoding="utf-8")

# Add a get_view_count function after get_intro_images
marker = "def archive_project(url, project_title, page, session, force=False):"

view_fn = '''def get_view_count(page):
    """Extract the view count using the data-testid attribute (JS-rendered)."""
    try:
        el = page.query_selector('[data-testid="project-view-count"]')
        if el:
            text = el.inner_text().strip()
            text = text.lower().replace(",", "")
            if text.endswith("m"):
                return int(float(text[:-1]) * 1_000_000)
            if text.endswith("k"):
                return int(float(text[:-1]) * 1_000)
            return int(text)
    except Exception:
        pass
    return 0


'''

if marker in content and "def get_view_count" not in content:
    content = content.replace(marker, view_fn + marker, 1)
    print("Added get_view_count function")
else:
    print("Marker not found or already patched")

path.write_text(content, encoding="utf-8")

# Now hook it into archive_project — find where data is extracted and call get_view_count
content = path.read_text(encoding="utf-8")
old_hook = "    title     = data.get(\"title\") or project_title"
new_hook = "    title     = data.get(\"title\") or project_title\n    views     = get_view_count(page)"

if old_hook in content and "views     = get_view_count" not in content:
    content = content.replace(old_hook, new_hook, 1)
    print("Hooked get_view_count into archive_project")
    path.write_text(content, encoding="utf-8")
else:
    print("Hook already present or marker not found")
