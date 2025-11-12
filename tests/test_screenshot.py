import re
from playwright.sync_api import expect

def test_takeScreenshot(page):
    page.wait_for_timeout(5000)
    page.goto("https://google.com/ncr")
    try:
        page.get_by_role("button",name="Accept all").click(timeout=5000)
    except:
        print("No popup to accept")
    page.get_by_role("combobox",name="Search").fill("Shahrukh Khan")
    page.keyboard.press("Enter")
    page.wait_for_timeout(15000)
    expect(page).to_have_title(re.compile("Shahrukh",re.I))

    