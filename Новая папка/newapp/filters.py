from django_filters import FilterSet, DateTimeFilter
from .models import Post
import django.forms


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],

        }








