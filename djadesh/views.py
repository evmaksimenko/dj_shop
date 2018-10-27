# from django.shortcuts import render
from django.views import generic
from .models import Item


class IndexView(generic.ListView):
    model = Item
    template_name = 'djadesh/index.html'


class ItemView(generic.DetailView):
    model = Item
    template_name = 'djadesh/item.html'
