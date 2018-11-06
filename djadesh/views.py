from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFit

from .models import Item


class IndexView(generic.ListView):
    model = Item
    template_name = 'djadesh/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.session.get('basket_items', []):
            self.request.session['basket_items'] = []
            self.request.session['basket_items_count'] = 0
            self.request.session['basket_total_price'] = 0
        context['basket_items_count'] = self.request.session.get('basket_items_count', 0)
        context['basket_total_price'] = self.request.session.get('basket_total_price', 0)
        return context


class ItemView(generic.DetailView):
    model = Item
    template_name = 'djadesh/item.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.session.get('basket_items', []):
            self.request.session['basket_items'] = []
            self.request.session['basket_items_count'] = 0
            self.request.session['basket_total_price'] = 0
        context['basket_items_count'] = self.request.session.get('basket_items_count', 0)
        context['basket_total_price'] = self.request.session.get('basket_total_price', 0)
        return context


def basket_add(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if not request.session.get('basket_items', []):
        request.session['basket_items'] = []
        request.session['basket_items_count'] = 0
        request.session['basket_total_price'] = 0
    store_quantity = item.store.quantity
    if store_quantity:
        request.session['basket_items'].append(item.id)
        request.session['basket_items_count'] += 1
        request.session['basket_total_price'] += item.price
    return HttpResponseRedirect(reverse('djadesh:basket'))


def basket(request):
    if not request.session.get('basket_items', []):
        return HttpResponseRedirect(reverse('djadesh:index'))
    items = []
    total_price = 0
    for item_id in request.session['basket_items']:
        item = get_object_or_404(Item, pk=item_id)
        total_price += item.price
        items.append(item)
    return render(request, 'djadesh/basket.html', {'items': items, 'total_price': total_price})


class Preview(ImageSpec):
    processors = [ResizeToFit(300, 300, False)]
    format = 'JPEG'
    options = {'quality': 90}


class MainImage(ImageSpec):
    processors = [ResizeToFit(500, 500, False)]
    format = 'JPEG'
    options = {'quality': 90}


register.generator('djadesh:preview', Preview)
register.generator('djadesh:mainimage', MainImage)