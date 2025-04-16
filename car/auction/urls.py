from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter()

router.register(r'users', UserProfileViewSet, basename='users')

urlpatterns = [

    path('brands/', BrandListAPIView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail'),

    path('car-models/', CarModelListAPIView.as_view(), name='car-model-list'),
    path('car-models/<int:pk>/', CarModelDetailAPIView.as_view(), name='car-model-detail'),
    path('cars/', CarListAPIView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarDetailAPIView.as_view(), name='car-detail'),
    path('cars/<int:pk>/edit/', CarUpdateDeleteAPIView.as_view(), name='car-update-delete'),

    path('auctions/', AuctionListAPIView.as_view(), name='auction-list'),
    path('auctions/<int:pk>/', AuctionDetailAPIView.as_view(), name='auction-detail'),

    path('bids/', BidListAPIView.as_view(), name='bid-list'),
    path('bids/<int:pk>/', BidDetailAPIView.as_view(), name='bid-detail'),

    path('feedbacks/', FeedbackListAPIView.as_view(), name='feedback-list'),
    path('feedbacks/<int:pk>/', FeedbackDetailAPIView.as_view(), name='feedback-detail'),
]
