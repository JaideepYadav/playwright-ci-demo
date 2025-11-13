import re
from playwright.sync_api import expect

def test_takeScreenshot(page):
    # wait a bit just to make sure page is loaded
    page.wait_for_timeout(2000)

    # open DuckDuckGo
    page.goto("https://duckduckgo.com", wait_until="domcontentloaded")

    search_box = page.locator("input[name='q']")
    search_box.fill("SRK")
    page.keyboard.press("Enter")

    first = page.locator('a[data-testid="result-title-a"], a.result__a').first
    first.wait_for(timeout=30000)

    # 3️⃣ Validate that result is visible
    expect(first).to_be_visible()


    # 5️⃣ Optional pause so you can see it in headed mode
    page.wait_for_timeout(3000)
