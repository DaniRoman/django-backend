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
    
    def test_not_saving_with_get_request(self):
        self.client.get('/api/list/')
        res = Item.objects.count()
        exp = 0
        assert res == exp
    
    def test_can_save_a_POST_request(self):
        
        self.client.post('/api/list/', data={'item_text':'A new list item'})
        saved_item = Item.objects.first()
        result = saved_item.text
        exp = 'A new list item'

        assert Item.objects.count() == 1 
        assert result == exp
    
    def test_redirects_after_post(self):
        response = self.client.post('/api/list/', data={'item_text':'A new list item'})
        assert response.status_code == 302
        assert response['location'] == '/api/list/'