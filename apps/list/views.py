from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.list.models import Item

# Create your views here.

def home(req):
    if req.method == 'POST':
        Item.objects.create(text = req.POST['item_text'])
        return redirect('/api/list/')
    
    return render(req, 'list/index.html')