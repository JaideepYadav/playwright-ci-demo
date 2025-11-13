from playwright.sync_api import Page, expect
import re

def test_title_search(page: Page):
    page.goto("https://en.wikipedia.org/wiki/Playwright", wait_until="domcontentloaded")
    expect(page).to_have_title(re.compile("Playwright", re.I))
