from django.urls import path

from prescription.views import UserView, UserDetailView, DrugsView, DrugsDetailView, PharmacyView, PharmacyDetailView, \
    BookingView, BookingDetailView, PrescriptionView, PrescriptionDetailView

urlpatterns = [
    path("user/", UserView.as_view(), name="user"),
    path("user-detail/<int:id>/", UserDetailView.as_view(), name="user-detail"),
    path("drugs/", DrugsView.as_view(), name="drugs"),
    path("drugs-detail/<int:id>/", DrugsDetailView.as_view(), name="drugs-detail"),
    path("pharmacy/", PharmacyView.as_view(), name="pharmacy"),
    path("pharmacy-detail/<int:id>/", PharmacyDetailView.as_view(), name="pharmacy-detail"),
    path("prescription/", PrescriptionView.as_view(), name="prescription"),
    path("prescription-detail/<int:id>/", PrescriptionDetailView.as_view(), name="prescription-detail"),
    path("booking/", BookingView.as_view(), name="booking"),
    path("booking-detail/<int:id>/", BookingDetailView.as_view(), name="booking-detail"),
]
