from playwright.sync_api import Page, expect
import pytest
@pytest.mark.parametrize("query", [
    "Playwright Python",
    "pytest fixtures",
    "browser automation",
])
def test_google_search_results(page: Page, query: str):

    # 1. Go to Google
    page.goto("https://www.google.com", wait_until="domcontentloaded")
    search_box = page.get_by_role("combobox", name="Search")
    search_box.fill(query)
    search_box.press("Enter")
    first_result = page.locator("h3").first
    first_result.wait_for(timeout=15000)  
    expect(first_result).to_be_visible()
    with page.expect_navigation():
        first_result.click()

    expect(page).not_to_have_url("https://www.google.com")
