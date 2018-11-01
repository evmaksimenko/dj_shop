from django.views import generic
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, ResizeToFit

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