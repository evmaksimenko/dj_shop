from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, item_id):
    return HttpResponse("Hello, world. You're at the details. #{}".format(item_id))
