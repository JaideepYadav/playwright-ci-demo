from playwright.sync_api import Page, expect
import re
def test_title_search(page:Page):
    page.goto('https://duckduckgo.com/?q=Playwright+pytest&ia=web')
    page.locator('a[data-testid="result-title-a"], a.result__a').first.wait_for(timeout=15000)
    expect(page).to_have_title(re.compile("Playwright",re.I))