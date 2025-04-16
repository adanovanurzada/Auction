from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'age',
                  'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh =RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, date):
        user = authenticate(**date)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Наверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                 'username': instance.username,
                 'email': instance.email,
        },
        'access': str(refresh.access_token),
        'refresh': str(refresh),

        }


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'role']



class BrandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name']


class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarModelListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()

    class Meta:
        model = CarModel
        fields = ['id', 'car_model', 'brand']


class CarModelDetailSerializer(serializers.ModelSerializer):
    brand = BrandListSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    car_model = serializers.StringRelatedField()
    seller = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'brand', 'car_model', 'year', 'price', 'seller']


class CarDetailSerializer(serializers.ModelSerializer):
    brand = BrandListSerializer(read_only=True)
    car_model = CarModelListSerializer(read_only=True)
    seller = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class AuctionListSerializer(serializers.ModelSerializer):
    car = CarListSerializer(read_only=True)

    class Meta:
        model = Auction
        fields = ['id', 'car', 'status', 'start_time', 'end_time']


class AuctionDetailSerializer(serializers.ModelSerializer):
    car = CarDetailSerializer(read_only=True)

    class Meta:
        model = Auction
        fields = '__all__'



class BidListSerializer(serializers.ModelSerializer):
    buyer = UserSimpleSerializer(read_only=True)
    auction = serializers.StringRelatedField()

    class Meta:
        model = Bid
        fields = ['id', 'auction', 'buyer',  'created_at']


class BidDetailSerializer(serializers.ModelSerializer):
    buyer = UserSimpleSerializer(read_only=True)
    auction = AuctionListSerializer(read_only=True)

    class Meta:
        model = Bid
        fields = '__all__'


class FeedbackListSerializer(serializers.ModelSerializer):
    seller = UserSimpleSerializer(read_only=True)
    buyer = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'seller', 'buyer', 'rating']


class FeedbackDetailSerializer(serializers.ModelSerializer):
    seller = UserSimpleSerializer(read_only=True)
    buyer = UserSimpleSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'
