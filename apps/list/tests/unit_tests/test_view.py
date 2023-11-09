import django
django.setup()
from django.test import TestCase, Client
from django.urls import resolve, reverse
from apps.list.views import home
from apps.list.models import Item

class TestListMain(TestCase):

    client = Client()
    view_uri = resolve('/api/list/')
    
    def test_list_root_url_resolves_to_home_page_view(self):
        
        assert self.view_uri.func == home

    def test_list_home_page_returns_correct_template(self):
        
        url = reverse('list')
        res = self.client.get(url)

        self.assertTemplateUsed('index.html')    
        assert res.status_code == 200
    
    def test_can_save_a_POST_request(self):
        
        res = self.client.post('/api/list/', data={'item_text':'A new list item'})
        self.assertTemplateUsed('index.html')    
        saved_item_text = Item.objects.first().text
        exp = 'A new list item'

        assert Item.objects.count() == 2 
        # assert saved_item_text == exp
        assert 'A new list item' in res.content.decode()