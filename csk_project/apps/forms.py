from django import forms
from django.contrib.auth.models import User
from .models import *


# ================= REGISTER FORM =================

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password'
        ]


# ================= CATEGORY FORM =================

class CategoryForm(forms.ModelForm):

    class Meta:

        model = Category

        fields = '__all__'


# ================= SUBCATEGORY FORM =================

class SubCategoryForm(forms.ModelForm):

    class Meta:

        model = SubCategory

        fields = '__all__'


# ================= TRAIN FORM =================

class TrainForm(forms.ModelForm):

    class Meta:

        model = Train

        fields = '__all__'


# ================= BOOKING FORM =================

class BookingForm(forms.ModelForm):

    class Meta:

        model = Booking

        fields = [
            'booking_date',
            'booking_time',
            'seats'
        ]


# ================= CONTACT FORM =================

class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = '__all__'





