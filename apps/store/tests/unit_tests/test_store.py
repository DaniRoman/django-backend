from django.test import TestCase, Client
from django.urls import resolve, reverse
from apps.store import views

import django
django.setup()

class TestStoreMain(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        res = resolve('/api/store/')
        assert res.func == views.home_page

    def test_home_page_returns_correct_template(self):
        client = Client()
        url = reverse('store')
        res = client.get(url)
        self.assertTemplateUsed('index.html')
               
        assert res.status_code == 200
 



        