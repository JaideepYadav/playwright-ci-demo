from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("query", [
    "Playwright",
    "Pytest",
    "Browser automation",
])
def test_wikipedia_search_results(page: Page, query: str):
    page.goto("https://en.wikipedia.org/wiki/Main_Page", wait_until="domcontentloaded")
    search_box = page.locator("input#searchInput")
    search_box.fill(query)
    search_box.press("Enter")

    # 4. Wait for results page to load (page heading must appear)
    heading = page.locator("#firstHeading")
    heading.wait_for(timeout=15000)
    expect(heading).to_be_visible()
    page.wait_for_timeout(2000)
