from django.contrib import admin


from .models import Item, ItemProperty, ItemImages, Store


class PropertyInline(admin.TabularInline):
    model = ItemProperty
    extra = 3


class ImageInline(admin.TabularInline):
    model = ItemImages
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