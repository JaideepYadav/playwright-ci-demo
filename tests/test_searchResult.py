from playwright.sync_api import Page, expect
import pytest

@pytest.mark.parametrize("query", [
    "Playwright Python",
    "pytest fixtures",
    "browser automation",
])
def test_duckduckgo_search_results(page: Page, query: str):
    page.goto("https://duckduckgo.com", wait_until="domcontentloaded")
    search_box = page.get_by_placeholder("Search the web without being tracked")
    search_box.fill(query)
    search_box.press("Enter")
    first_result = page.locator('a[data-testid="result-title-a"], a.result__a').first
    first_result.wait_for(timeout=15000)
    expect(first_result).to_be_visible()
    with page.expect_navigation():
        first_result.click()
    expect(page).not_to_have_url("https://duckduckgo.com")
    page.wait_for_timeout(3000)
