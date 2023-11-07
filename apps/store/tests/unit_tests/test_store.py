from django.test import TestCase, Client
from django.urls import resolve, reverse
from apps.store import views

import django
django.setup()


def test_root_url_resolves_to_home_page_view():
    res = resolve('/api/store/')
    assert res.func == views.home_page

def test_home_page_returns_correct_html():
    
    client = Client()
    url = reverse('store')
    res = client.get(url)
    # self.assertTemplateUsed(res, 'home.html')
    template_name_list = [template for template in res.templates]
    print(template_name_list)

    assert 'index' in template_name_list



    