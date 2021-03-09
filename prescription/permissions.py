from rest_framework import permissions


class CreatePrescriptionPermission(permissions.BasePermission):
    """
    Only user with role doctor can generate prescription
    """

    def has_permission(self, request, view):
        return True if request.user.type == "doctor" else False


class CreateBookingPermission(permissions.BasePermission):
    """
    Only user with role patient can order medicines
    """

    def has_permission(self, request, view):
        return True if request.user.type == "patient" else False
