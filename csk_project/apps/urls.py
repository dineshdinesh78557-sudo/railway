from django.urls import path
from . import views

urlpatterns = [

    # HOME
    path('', views.home, name='home'),

    # AUTH
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # DASHBOARD
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/',
         views.admin_dashboard,
         name='admin_dashboard'),

    # CATEGORY
    path('add-category/',
         views.add_category,
         name='add_category'),

    path('category-list/',
         views.category_list,
         name='category_list'),

    path('edit-category/<int:pk>/',
         views.edit_category,
         name='edit_category'),

    path('delete-category/<int:pk>/',
         views.delete_category,
         name='delete_category'),

    # SUBCATEGORY
    path('add-subcategory/',
         views.add_subcategory,
         name='add_subcategory'),

    path('subcategory-list/',
         views.subcategory_list,
         name='subcategory_list'),

    # TRAIN
    path('add-train/',
         views.add_train,
         name='add_train'),

    path('train-list/',
         views.train_list,
         name='train_list'),

    path('train-detail/<int:pk>/',
         views.train_detail,
         name='train_detail'),

    path('edit-train/<int:pk>/',
         views.edit_train,
         name='edit_train'),

    path('delete-train/<int:pk>/',
         views.delete_train,
         name='delete_train'),

    # BOOKING
    path('book-train/<int:pk>/',
         views.book_train,
         name='book_train'),

    path('booking-list/',
         views.booking_list,
         name='booking_list'),

    path('delete-booking/<int:pk>/',
         views.delete_booking,
         name='delete_booking'),

    # PAYMENT
    path('payment/<int:pk>/',
         views.payment,
         name='payment'),

    # DOWNLOAD TICKET
    path('download-ticket/<int:pk>/',
         views.download_ticket,
         name='download_ticket'),

    # SEARCH
    path('search/',
         views.search,
         name='search'),

    # REPORT
    path('report/',
         views.report,
         name='report'),

    # PAGES
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),


   

]
