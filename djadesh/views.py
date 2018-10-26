# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Item


class IndexView(ListView):
    model = Item
    template_name = 'djadesh/index.html'


def detail(request, item_id):
    return HttpResponse("Hello, world. You're at the details. #{}".format(item_id))
