import django_filters
from .models import ProductVariantPrice

class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = ProductVariantPrice
        fields = ('price', 'stock', 'product')