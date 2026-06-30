"""
After download_archive.py has been updated to capture views, this script
updates projects.json with the view counts captured during archiving.

This works by reading view counts that download_archive.py will print/log,
but the cleanest approach is to have download_archive.py update projects.json
directly. Let's patch that in.

Run from repo root: python fix_views2.py
"""
from pathlib import Path

path = Path("scraper/download_archive.py")
content = path.read_text(encoding="utf-8")

# Find where projects.json might be loaded, or add loading at top of archive_project
# We'll update PROJECTS_JSON entries directly after computing views

old = '''    title     = data.get("title") or project_title
    views     = get_view_count(page)'''

new = '''    title     = data.get("title") or project_title
    views     = get_view_count(page)

    # Update the view count in projects.json for this URL
    try:
        projects_path = Path(__file__).parent.parent / "projects.json"
        if projects_path.exists():
            import json as _json
            with open(projects_path, encoding="utf-8") as f:
                all_projects = _json.load(f)
            changed = False
            for p in all_projects:
                if p.get("url") == url and views:
                    if p.get("views") != views:
                        p["views"] = views
                        changed = True
                    break
            if changed:
                with open(projects_path, "w", encoding="utf-8") as f:
                    _json.dump(all_projects, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"    [warn] could not update projects.json views: {e}")'''

if old in content:
    content = content.replace(old, new, 1)
    print("Added projects.json view update")
else:
    print("ERROR: marker not found — run fix_views.py first")

path.write_text(content, encoding="utf-8")
