from django.test import TestCase, Client
from django.urls import resolve, reverse
from apps.core.views import homeSI

import django
django.setup()

class TestUo(TestCase):

    def setUp(self) -> None:
       self.client = Client()
    
    def test_correct_func(self):
        res = resolve('/api/core/')
        assert res.func == homeSI
        
    def test_uno(self):
        url = reverse('core')
        res = self.client.get(url)
        print("")
        self.assertTemplateUsed("index.html")
        pass
