import subprocess
import pytest

from playwright.sync_api import Page, expect


@pytest.fixture(scope='module', autouse=True)
def run_django_server():
    command = ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']
    proces = subprocess.Popen(command)
    yield
    proces.terminate()

def test_home_page(page: Page):
    url = 'django-app/api/store'
    page.goto(url)
    expect(page.get_by_role("heading", name="Sample Store")).to_be_visible()