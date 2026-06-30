"""
Debug why view counts are missing for most projects.
Run from repo root: python debug_views.py
"""
import requests
from bs4 import BeautifulSoup
import re

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
}

# Test on a project that's showing "--" for views
URL = "https://www.instructables.com/Shotgun-Shell-Canisters/"

r = requests.get(URL, headers=HEADERS, timeout=20)
soup = BeautifulSoup(r.text, "html.parser")

print("Testing selectors:")
for sel in ["span.views-count", "div.views", "[data-views]"]:
    els = soup.select(sel)
    print(f"  {sel}: {len(els)} found")

# Search for anything containing "view" case-insensitive
print("\nSearching for view-related text in page...")
for el in soup.find_all(string=re.compile(r"\d[\d,.]*[KkMm]?\s*[Vv]iews?")):
    parent = el.parent
    print(f"  Text: {repr(el.strip()[:50])}, parent tag: {parent.name}, class: {parent.get('class')}")

# Look for elements with "view" in class name
print("\nElements with 'view' in class name:")
for el in soup.find_all(class_=re.compile("view", re.I)):
    print(f"  tag={el.name}, class={el.get('class')}, text={el.get_text(strip=True)[:40]}")
