from django.views import generic
from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill, ResizeToFit, SmartResize

from .models import Item


class IndexView(generic.ListView):
    model = Item
    template_name = 'djadesh/index.html'


class ItemView(generic.DetailView):
    model = Item
    template_name = 'djadesh/item.html'


class Preview(ImageSpec):
    processors = [ResizeToFit(300, 300, False)]
    format = 'JPEG'
    options = {'quality': 90}


class Thumbnail(ImageSpec):
    processors = [ResizeToFill(50, 50)]
    format = 'JPEG'
    options = {'quality': 60}


register.generator('djadesh:preview', Preview)
register.generator('djadesh:thumbnail', Thumbnail)