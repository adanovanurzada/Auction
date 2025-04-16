from django_filters import FilterSet
from .models import *


class BrandFilter(FilterSet):
    class Meta:
        model = Brand
        fields = {
            'brand_name': ['exact'],
        }



class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'price': ['gt', 'lt'],
            'year': ['exact', 'gt', 'lt'],
        }


class AuctionFilter(FilterSet):
    class Meta:
        model = Auction
        fields = {
            'start_price': ['gt', 'lt'],
            'start_time': ['gt', 'lt'],
            'status': ['exact'],
        }


class BidFilter(FilterSet):
    class Meta:
        model = Bid
        fields = {
            'auction__id': ['exact'],
            'amount': ['gt', 'lt'],
            'created_at': ['gt', 'lt'],
        }


class FeedbackFilter(FilterSet):
    class Meta:
        model = Feedback
        fields = {
            'rating': ['gt', 'lt'],
            'buyer__id': ['exact'],
        }
