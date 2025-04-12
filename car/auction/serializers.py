from rest_framework import serializers
from .models import *

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CarModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class AuctionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = '__all__'

class BidSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = '__all__'