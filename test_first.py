from playwright.sync_api import Page, expect
import re

def test_duckduckgo_click_first_result(page: Page):
    # open results directly to avoid home redirects
    page.goto("https://duckduckgo.com/?q=Playwright+pytest&ia=web")

    # first result (supports both classic and new DDG UI)
    result = page.locator('a[data-testid="result-title-a"], a.result__a').first
    result.wait_for(timeout=15000)

    # basic sanity check on the results page
    expect(page).to_have_title(re.compile("Playwright", re.I))

    # click and wait for **same-tab** navigation
    with page.expect_navigation():
        result.click()
    page.wait_for_timeout(5000)
    # assert we actually left DuckDuckGo
    expect(page).not_to_have_url(re.compile(r"duckduckgo\.com"))
    # (optional) prove we opened something meaningful
    expect(page).to_have_url(re.compile(r"^https?://"))
