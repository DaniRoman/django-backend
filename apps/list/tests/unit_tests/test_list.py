from django.test import TestCase, Client
from django.urls import resolve, reverse
from apps.list.views import home

import django
django.setup()

class TestListMain(TestCase):

    def test_list_root_url_resolves_to_home_page_view(self):
        res = resolve('/api/list/')
        assert res.func == home

    def test_list_home_page_returns_correct_template(self):
        client = Client()
        url = reverse('list')
        res = client.get(url)
        self.assertTemplateUsed('index.html')
               
        assert res.status_code == 200
 