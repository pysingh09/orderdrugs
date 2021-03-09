from rest_framework import serializers

from prescription.models import User, Drugs, Pharmacy, Booking, Prescription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_staff', 'is_active', 'last_login')


class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = "__all__"


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"
