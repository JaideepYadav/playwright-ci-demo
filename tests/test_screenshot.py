import re
from playwright.sync_api import expect

def test_takeScreenshot(page):
    page.wait_for_timeout(5000)
    page.goto("https://duckduckgo.com")
    page.get_by_placeholder("Search the web without being tracked").fill("SRK")
    page.keyboard.press("Enter")
    first = page.locator('a[data-testid="result-title-a"], a.result__a').first
    first.wait_for(timeout=20000)
    expect(first).to_be_visible()

    