import re
from playwright.sync_api import Playwright, sync_playwright, expect



def test_add_todo_tasko(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий плайрайт")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("link", name="Completed").click()

    # ---------------------
    context.close()
    browser.close()


