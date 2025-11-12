from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="chrome", headless=False)
    page = browser.new_page()
    page.goto("https://duckduckgo.com")
    page.fill("input[name='q']", "Playwright Python tutorial")
    page.keyboard.press("Enter")
    page.wait_for_timeout(8000)
    browser.close()
