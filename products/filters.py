
from django_filters import rest_framework as django_filters
from .models import Product,Review


class ProductFilter(django_filters.FilterSet):
    min_price=django_filters.NumberFilter(field_name="price",lookup_expr='gte')
    max_price=django_filters.NumberFilter(field_name="price",lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category','min_price','max_price']


class ReviewFilter(django_filters.FilterSet):
    min_rating=django_filters.NumberFilter(field_name="rating",lookup_expr='gte')
    max_rating=django_filters.NumberFilter(field_name="rating",lookup_expr='lte')

    class Meta:
        model = Review
        fields = ['content','min_rating','max_rating']