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

# @pytest.fixture(scope='function', autouse=True)
# def check_if_server_is_runnig() -> bool:
#     max_attemps = 10
#     c = Client()
#     url = 'http://0.0.0.0:8000/api/list/'

#     for _ in range(max_attemps):
#         try:
#             if c.get(url).status_code == 200:
#                 return True 
#         except exceptions.RequestException as e:
#             print('Error al realizar la solicitud:', e)
#         print(f"atemp num {_}" ) 
#         time.sleep(1)

    


# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")

#     # Click the get started link.
#     page.get_by_role("link", name="Get started").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def test_list_home_page(page: Page):

    url = "http://0.0.0.0:8000/api/list"
    page.goto(url)
    
    expect(page.get_by_role("heading", name="List Home Site")).to_be_visible()