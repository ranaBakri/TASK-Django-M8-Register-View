from datetime import datetime
from flights import serializers
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView
from flights.models import Booking, Flight
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer, UserCreateSerializer


class FlightsList(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class BookingsList(ListAPIView):
    queryset = Booking.objects.filter(date__gte=datetime.today())
    serializer_class = BookingSerializer


class BookingDetails(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailsSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class UpdateBooking(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = UpdateBookingSerializer
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class CancelBooking(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "booking_id"


class BookFlight(CreateAPIView):
    serializer_class = serializers.UpdateBookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,
                        flight_id=self.kwargs["flight_id"])


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
