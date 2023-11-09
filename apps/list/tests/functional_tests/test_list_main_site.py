import subprocess
import pytest
import time
import django

from requests import exceptions
from playwright.sync_api import Page, expect
from django.test import Client

django.setup()

@pytest.fixture(scope='session', autouse=True)
def run_django_server():
    command = ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']
    proces = subprocess.Popen(command)
    yield
    proces.terminate()

@pytest.fixture(scope='module', autouse=True)
def wait():
    time.sleep(2)

def check_for_row_in_list_table(page: Page, row_text):
    table = page.locator('table#id_table')
    rows = table.locator('tr#id_list_table')
    assert row_text in [row.name for row in rows]

def test_list_home_page(page: Page):
    # Edith has heard about a cool new online to-do app. She goes
    # to check out its homepage
    url = "http://0.0.0.0:8000/api/list"
    page.goto(url)
    # She notices the page title and header mention List Home Site"
    expect(page.get_by_role("heading", name="List Home Site")).to_be_visible()
    # She is invited to enter a to-do item straight away
    # She types "Buy peacock feathers" into a text box (Edith's hobby
	# is tying fly-fishing lures)
    inputbox = expect(page.get_by_placeholder('Enter a To Do Item')).to_be_visible()
    # When she hits enter, the page updates, and now the page lists
	# "1: Buy peacock feathers" as an item in a to-do list table
    inputbox.fill('Buy peacock feathers').click()
    time.sleep(1)
    check_for_row_in_list_table('1: Buy peacock feathers')

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very
    # methodical)
    inputbox = expect(page.get_by_placeholder('Enter a To Do Item')).to_be_visible()
    inputbox.fill('Use peacock feathers to make a fly').click()
    time.sleep(1)
    # The page updates again, and now shows both items on her list
    check_for_row_in_list_table('1: Buy peacock feathers')
    check_for_row_in_list_table('2: Use peacock feathers to make a fly')