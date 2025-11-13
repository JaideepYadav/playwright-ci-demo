from playwright.sync_api import expect

def test_takeScreenshot(page):
    page.goto("https://en.wikipedia.org/wiki/Main_Page", wait_until="domcontentloaded")

    page.locator("#searchInput").fill("Shah Rukh Khan")
    page.keyboard.press("Enter")

    first = page.locator("h1").first
    first.wait_for(timeout=10000)
    expect(first).to_be_visible()

    page.wait_for_timeout(3000)
