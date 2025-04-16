from .serializers import *
from .models import *
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsOwnerOrReadOnly


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BrandFilter
    search_fields = ['brand_name']


class BrandDetailAPIView(generics.RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializer


class CarModelListAPIView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelListSerializer


class CarModelDetailAPIView(generics.RetrieveAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelDetailSerializer


class CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = CarFilter
    ordering_fields = ['price', 'year']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CarDetailAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CarUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class AuctionListAPIView(generics.ListAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = AuctionFilter
    search_fields = ['status']
    ordering_fields = ['start_price', 'start_time']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class AuctionDetailAPIView(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionDetailSerializer


class BidListAPIView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BidFilter
    search_fields = ['auction__id']
    ordering_fields = ['created_at', 'amount']
    permission_classes = [IsAuthenticatedOrReadOnly]


class BidDetailAPIView(generics.RetrieveAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidDetailSerializer


class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FeedbackFilter
    search_fields = ['buyer__id']
    ordering_fields = ['rating']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class FeedbackDetailAPIView(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackDetailSerializer
