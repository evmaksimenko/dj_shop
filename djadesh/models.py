from django.db import models


class Item(models.Model):
    code = models.CharField(max_length=8)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024, blank=True, default="")
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class ItemProperty(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    property_name = models.CharField(max_length=200)
    property_value = models.CharField(max_length=200)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.property_name


class ItemImages(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    img_name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='items', null=True)

    def __str__(self):
        return self.img_name


class Store(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.quantity)
