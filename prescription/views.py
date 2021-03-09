from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings

from prescription.models import User, Drugs, Pharmacy, Booking, Prescription, Medicines
from prescription.permissions import CreatePrescriptionPermission, CreateBookingPermission
from prescription.serializers import UserSerializer, DrugsSerializer, PharmacySerializer, BookingSerializer, \
    PrescriptionSerializer


# Create your views here.


class UserView(generics.ListCreateAPIView):
    """
    Create user instance,
    generate user token,
    and get all user list
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # generate user token on registration
        Token.objects.get_or_create(user=serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj


class DrugsView(generics.ListCreateAPIView):
    serializer_class = DrugsSerializer
    queryset = Drugs.objects.all()
    permission_classes = (AllowAny,)


class DrugsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DrugsSerializer
    queryset = Drugs.objects.all()
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj


class PharmacyView(generics.ListCreateAPIView):
    serializer_class = PharmacySerializer
    queryset = Pharmacy.objects.all()
    permission_classes = (AllowAny,)


class PharmacyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PharmacySerializer
    queryset = Pharmacy.objects.all()
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj


class PrescriptionView(generics.CreateAPIView, generics.UpdateAPIView):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()
    permission_classes = (IsAuthenticated, CreatePrescriptionPermission)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # create multiple medicines object
        data = [Medicines(prescription=serializer.instance, drugs_id=vals.get('drugs'), quantity=vals.get('quantity'))
                for vals in self.request.data.get('medicines')]
        Medicines.objects.bulk_create(data)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


class PrescriptionDetailView(generics.RetrieveAPIView):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj


class BookingView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated, CreateBookingPermission)


class BookingDetailView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = (AllowAny,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('id'))
        self.check_object_permissions(self.request, obj)
        return obj
