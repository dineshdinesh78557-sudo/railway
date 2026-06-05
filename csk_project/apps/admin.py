from django.contrib import admin
from .models import *


# ================= CATEGORY ADMIN =================

class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name']


admin.site.register(Category, CategoryAdmin)


# ================= SUBCATEGORY ADMIN =================

class SubCategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'category', 'name']


admin.site.register(SubCategory, SubCategoryAdmin)


# ================= TRAIN ADMIN =================

class TrainAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
        'from_place',
        'to_place',
        'price',
        'available_seats',
        'date',
        'time'
    ]

    search_fields = ['name']

    list_filter = ['category']


admin.site.register(Train, TrainAdmin)


# ================= BOOKING ADMIN =================

class BookingAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'user',
        'train',
        'booking_date',
        'seats',
        'total_price',
        'payment_status'
    ]


admin.site.register(Booking, BookingAdmin)


# ================= PAYMENT ADMIN =================

class PaymentAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'booking',
        'payment_id',
        'amount',
        'payment_method',
        'paid_on'
    ]


admin.site.register(Payment, PaymentAdmin)


# ================= CONTACT ADMIN =================

class ContactAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name',
        'email',
        'subject',
        'created_at'
    ]


admin.site.register(Contact, ContactAdmin)