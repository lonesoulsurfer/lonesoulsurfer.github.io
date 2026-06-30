"""
Confirm the data-testid view selector and check what attribute holds 'view' specifically.
"""
from playwright.sync_api import sync_playwright
import time

URL = "https://www.instructables.com/Shotgun-Shell-Canisters/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded", timeout=30000)
    time.sleep(3)

    els = page.query_selector_all('[data-testid*="view"]')
    for el in els:
        testid = el.get_attribute('data-testid')
        text = el.inner_text().strip()
        print(f"data-testid={testid}, text={repr(text)}")
        # Check parent for context
        parent_html = el.evaluate('el => el.parentElement.outerHTML')
        print(f"  parent HTML: {parent_html[:200]}")

    browser.close()
