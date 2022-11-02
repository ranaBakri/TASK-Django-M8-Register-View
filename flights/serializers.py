from flights.models import Booking, Flight
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["destination", "time", "price", "id"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "id"]


class BookingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["flight", "date", "passengers", "id"]


class UpdateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["date", "passengers"]


user = get_user_model


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(writeonly=True)

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name"]

        def create(self, validated_data):
            username = validated_data["username"]
            password = validated_data["password"]
            new_user = User(username=username)
            new_user.set_password(password)
            new_user.save()
            return validated_data
