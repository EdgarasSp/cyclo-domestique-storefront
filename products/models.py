from django.db import models


class Division(models.Model):

    class Meta:
        verbose_name_plural = 'Divisions'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    division = models.ForeignKey('Division', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    size = models.CharField(max_length=254, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=0, default=10)
    color = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=254, null=True, blank=True)
    full_description = models.TextField(blank=True, null=True)
    key_features = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1,
                                 null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
