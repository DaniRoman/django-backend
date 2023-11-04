
from playwright.sync_api import Page, expect


def test_prueba(page: Page):
    page.goto("https://playwright.dev/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    