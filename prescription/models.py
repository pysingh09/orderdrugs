from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.db.models.signals import pre_save
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    phone = PhoneNumberField(null=False, blank=False)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10)

    class Meta:
        abstract = True


class User(AbstractBaseUser, Address, TimeStamp):
    """
    Represents a user profile inside our system.
    """

    SEX = (("male", "Male"), ("female", "Female"), ("other", "Other"))
    USER_TYPE = (("doctor", "Doctor"), ("chemist", "Chemist"), ("patient", "Patient"))

    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.PositiveIntegerField(default=0)
    sex = models.CharField(max_length=40, choices=SEX)
    type = models.CharField(max_length=40, choices=USER_TYPE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username', 'age', 'sex', 'type']

    def get_full_name(self):
        """Used to get a users full name."""
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        """Used to get a users short name."""
        return self.first_name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""
        return self.email


class Drugs(TimeStamp):
    """
    Represents a drugs inside our system.
    """
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    benefit = models.TextField(null=True, blank=True)
    side_effect = models.TextField(null=True, blank=True)
    advice = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Pharmacy(Address, TimeStamp):
    """
    Represents a pharmacy inside our system.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drugs = models.ManyToManyField(Drugs)
    website = models.URLField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Prescription(TimeStamp):
    """
    Represents a prescription inside our system.
    """
    symptoms = models.TextField()
    precautions = models.TextField(null=True, blank=True)
    medicines = models.ManyToManyField(Drugs, through="Medicines", related_name="prescribed_medicine")
    prescriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient")

    def __str__(self):
        return self.symptoms


class Medicines(models.Model):
    """
    Represents a medicines inside our system.
    """
    drugs = models.ForeignKey(Drugs, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="medicines_prescription")

    def __str__(self):
        return self.prescription.symptoms


class Booking(TimeStamp):
    """
    Represents a booking inside our system.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    user_prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="user_prescription")
    amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}-{self.amount}"


def save_amount(sender, instance, **kwargs):
    """
    To calculate drugs amount and save in booking on creation
    """
    medicines = Medicines.objects.filter(prescription=instance.user_prescription)
    amount = sum([medicine.quantity * medicine.drugs.price for medicine in medicines])
    instance.amount = amount


pre_save.connect(save_amount, sender=Booking)
