from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFit

from .models import Item


class DefaultShopMixin():
    model = Item
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.session.get('basket_items', []):
            self.request.session['basket_items'] = []
            self.request.session['basket_items_count'] = 0
            self.request.session['basket_total_price'] = 0
        context['basket_items_count'] = \
            self.request.session.get('basket_items_count', 0)
        context['basket_total_price'] = \
            self.request.session.get('basket_total_price', 0)
        return context


class IndexView(DefaultShopMixin, generic.ListView):
    template_name = 'djadesh/index.html'
    paginate_by = 2


class ItemView(DefaultShopMixin, generic.DetailView):
    template_name = 'djadesh/item.html'


class BasketCount(generic.View):
    def post(self, request, *args, **kwargs):
        item = get_object_or_404(Item, pk=kwargs['item_id'])
        if not request.session.get('basket_items', []):
            request.session['basket_items'] = []
            request.session['basket_items_count'] = 0
            request.session['basket_total_price'] = 0
        store_quantity = item.store.quantity
        if store_quantity:
            request.session['basket_items'].append(item.id)
            request.session['basket_items_count'] += 1
            request.session['basket_total_price'] += item.price
        return redirect('djadesh:basket')


class Basket(generic.View):
    def get(self, request, *args, **kwargs):
        if not request.session.get('basket_items', []):
            return redirect('djadesh:index')
        items = []
        total_price = 0
        for item_id in request.session['basket_items']:
            item = get_object_or_404(Item, pk=item_id)
            total_price += item.price
            items.append(item)
        return render(
            request,
            'djadesh/basket.html',
            {'items': items, 'total_price': total_price}
        )

    def post(self, request, *args, **kwargs):
        return redirect('djadesh:basket')


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
