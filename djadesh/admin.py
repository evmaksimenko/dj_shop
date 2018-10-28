from django.contrib import admin


from .models import Item, ItemProperty, ItemImage, Store


class PropertyInline(admin.TabularInline):
    model = ItemProperty
    extra = 5


class ImageInline(admin.TabularInline):
    model = ItemImage
    extra = 3


class ItemAdmin(admin.ModelAdmin):
    inlines = [
        PropertyInline,
        ImageInline,
    ]


admin.site.register(Item, ItemAdmin)
# admin.site.register(ItemProperty)
# admin.site.register(ItemImages)
admin.site.register(Store)