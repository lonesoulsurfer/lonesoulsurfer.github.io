"""
Debug view counts using Playwright (renders JS).
Run from repo root: python debug_views2.py
"""
from playwright.sync_api import sync_playwright
import re
import time

URL = "https://www.instructables.com/Shotgun-Shell-Canisters/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=30000)
    time.sleep(3)

    # Search for any text matching view count pattern
    content = page.content()
    matches = re.findall(r'[\d,.]+[KkMm]?\s*[Vv]iews?', content)
    print(f"Regex matches in HTML: {matches[:10]}")

    # Try common selectors
    selectors = [
        '[class*="view"]',
        '[class*="View"]',
        '[class*="stat"]',
        '[class*="Stat"]',
        '[data-testid*="view"]',
        'span:has-text("views")',
    ]
    for sel in selectors:
        try:
            els = page.query_selector_all(sel)
            print(f"\n{sel}: {len(els)} found")
            for el in els[:3]:
                txt = el.inner_text().strip()[:60]
                cls = el.get_attribute('class') or ''
                print(f"  text={repr(txt)}, class={cls[:50]}")
        except Exception as e:
            print(f"{sel}: error {e}")

    browser.close()
