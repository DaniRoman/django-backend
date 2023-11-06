from django.urls import resolve
from django.test import Client
from playwright.sync_api import Page, expect
from apps.core import views

import django
django.setup()

def test_root_url_resolves_to_home_page_view():
    res = resolve('/')
    assert res.func == views.home_page

def test_home_page_returns_correct_html():
    client = Client()
    res = client.get('/')
    cont = res.content
    assert b'<html>' in cont
    assert b'</html>' in cont