from django.db import models
from django.contrib.auth.models import User


# ================= CATEGORY =================

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ================= SUBCATEGORY =================

class SubCategory(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ================= TRAIN =================

class Train(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    subcategory = models.ForeignKey(
        SubCategory,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=200)

    from_place = models.CharField(max_length=200)

    to_place = models.CharField(max_length=200)

    description = models.TextField()

    price = models.IntegerField()

    image = models.ImageField(upload_to='trains/')

    available_seats = models.IntegerField()

    date = models.DateField()

    time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ================= BOOKING =================

class Booking(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    train = models.ForeignKey(
        Train,
        on_delete=models.CASCADE
    )

    booking_date = models.DateField()

    booking_time = models.TimeField()

    seats = models.IntegerField()

    total_price = models.IntegerField()

    payment_status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# ================= PAYMENT =================

class Payment(models.Model):

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE
    )

    payment_id = models.CharField(max_length=200)

    amount = models.IntegerField()

    payment_method = models.CharField(max_length=100)

    paid_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


# ================= CONTACT =================

class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    





