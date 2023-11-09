from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(req):
    return render(req, 'list/index.html', {
        'new_item_text': req.POST.get('item_text','')
    })