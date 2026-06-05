from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime


# ================= HOME =================

def home(request):

    query = request.GET.get('q')

    trains = Train.objects.all().order_by('-id')

    if query:
        trains = trains.filter(name__icontains=query)

    context = {
        'trains': trains
    }

    return render(request, 'home.html', context)


# ================= REGISTER =================

def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        user = form.save(commit=False)

        password = form.cleaned_data['password']

        user.set_password(password)

        user.save()

        messages.success(request, "Registration Successful")

        return redirect('login')

    return render(request, 'register.html', {'form': form})


# ================= LOGIN =================

def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,
                            password=password)

        if user:

            login(request, user)

            if user.is_superuser:
                return redirect('admin_dashboard')

            return redirect('dashboard')

        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


# ================= LOGOUT =================

def user_logout(request):

    logout(request)

    return redirect('home')


# ================= USER DASHBOARD =================

@login_required
def dashboard(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-id')

    total_bookings = bookings.count()

    context = {
        'bookings': bookings,
        'total_bookings': total_bookings
    }

    return render(request,
                  'dashboard.html',
                  context)


# ================= ADMIN DASHBOARD =================

@login_required
def admin_dashboard(request):

    total_trains = Train.objects.count()

    total_bookings = Booking.objects.count()

    total_users = User.objects.count()

    total_categories = Category.objects.count()

    context = {

        'total_trains': total_trains,
        'total_bookings': total_bookings,
        'total_users': total_users,
        'total_categories': total_categories,

    }

    return render(request,
                  'admin_dashboard.html',
                  context)


# ================= ADD CATEGORY =================

@login_required
def add_category(request):

    form = CategoryForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(request, "Category Added")

        return redirect('category_list')

    return render(request,
                  'add_category.html',
                  {'form': form})


# ================= CATEGORY LIST =================

@login_required
def category_list(request):

    categories = Category.objects.all()

    return render(request,
                  'category_list.html',
                  {'categories': categories})


# ================= EDIT CATEGORY =================

@login_required
def edit_category(request, pk):

    category = get_object_or_404(Category, id=pk)

    form = CategoryForm(request.POST or None,
                        instance=category)

    if form.is_valid():

        form.save()

        messages.success(request, "Category Updated")

        return redirect('category_list')

    return render(request,
                  'add_category.html',
                  {'form': form})


# ================= DELETE CATEGORY =================

@login_required
def delete_category(request, pk):

    category = get_object_or_404(Category, id=pk)

    category.delete()

    messages.success(request, "Category Deleted")

    return redirect('category_list')


# ================= ADD SUBCATEGORY =================

@login_required
def add_subcategory(request):

    form = SubCategoryForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(request, "SubCategory Added")

        return redirect('subcategory_list')

    return render(request,
                  'add_subcategory.html',
                  {'form': form})


# ================= SUBCATEGORY LIST =================

@login_required
def subcategory_list(request):

    subcategories = SubCategory.objects.all()

    return render(request,
                  'subcategory_list.html',
                  {'subcategories': subcategories})


# ================= ADD TRAIN =================

@login_required
def add_train(request):

    form = TrainForm(request.POST or None,
                     request.FILES or None)

    if form.is_valid():

        form.save()

        messages.success(request, "Train Added")

        return redirect('train_list')

    return render(request,
                  'add_train.html',
                  {'form': form})


# ================= TRAIN LIST =================

def train_list(request):

    trains = Train.objects.all().order_by('-id')

    return render(request,
                  'train_list.html',
                  {'trains': trains})


# ================= TRAIN DETAILS =================

def train_detail(request, pk):

    train = get_object_or_404(Train, id=pk)

    return render(request,
                  'train_detail.html',
                  {'train': train})


# ================= EDIT TRAIN =================

@login_required
def edit_train(request, pk):

    train = get_object_or_404(Train, id=pk)

    form = TrainForm(request.POST or None,
                     request.FILES or None,
                     instance=train)

    if form.is_valid():

        form.save()

        messages.success(request, "Train Updated")

        return redirect('train_list')

    return render(request,
                  'add_train.html',
                  {'form': form})


# ================= DELETE TRAIN =================

@login_required
def delete_train(request, pk):

    train = get_object_or_404(Train, id=pk)

    train.delete()

    messages.success(request, "Train Deleted")

    return redirect('train_list')


# ================= BOOK TRAIN =================

@login_required
def book_train(request, pk):

    train = get_object_or_404(Train, id=pk)

    form = BookingForm(request.POST or None)

    if form.is_valid():

        booking = form.save(commit=False)

        booking.user = request.user

        booking.train = train

        booking.total_price = train.price * booking.seats

        booking.payment_status = True

        booking.save()

        messages.success(request, "Ticket Booked Successfully")

        return redirect('dashboard')

    context = {
        'form': form,
        'train': train
    }

    return render(request,
                  'booking.html',
                  context)


# ================= BOOKING LIST =================

@login_required
def booking_list(request):

    bookings = Booking.objects.all().order_by('-id')

    return render(request,
                  'booking_list.html',
                  {'bookings': bookings})


# ================= DELETE BOOKING =================

@login_required
def delete_booking(request, pk):

    booking = get_object_or_404(Booking, id=pk)

    booking.delete()

    messages.success(request, "Booking Deleted")

    return redirect('booking_list')


# ================= PAYMENT =================

@login_required
def payment(request, pk):

    booking = get_object_or_404(Booking, id=pk)

    payment = Payment.objects.create(
        booking=booking,
        payment_id="PAY" + str(datetime.datetime.now().timestamp()),
        amount=booking.total_price
    )

    booking.payment_status = True

    booking.save()

    messages.success(request, "Payment Successful")

    return redirect('dashboard')


# ================= DOWNLOAD TICKET =================

@login_required
def download_ticket(request, pk):

    booking = get_object_or_404(Booking, id=pk)

    response = HttpResponse(content_type='text/plain')

    response['Content-Disposition'] = (
        f'attachment; filename="ticket_{booking.id}.txt"'
    )

    response.write(f"Railway Ticket\n")
    response.write(f"====================\n")
    response.write(f"User : {booking.user.username}\n")
    response.write(f"Train : {booking.train.name}\n")
    response.write(f"From : {booking.train.from_place}\n")
    response.write(f"To : {booking.train.to_place}\n")
    response.write(f"Seats : {booking.seats}\n")
    response.write(f"Total : ₹{booking.total_price}\n")

    return response


# ================= SEARCH =================

def search(request):

    query = request.GET.get('q')

    trains = Train.objects.filter(
        name__icontains=query
    )

    return render(request,
                  'search.html',
                  {'trains': trains})


# ================= REPORT =================

@login_required
def report(request):

    bookings = Booking.objects.all()

    total_income = 0

    for i in bookings:
        total_income += i.total_price

    context = {
        'bookings': bookings,
        'total_income': total_income
    }

    return render(request,
                  'report.html',
                  context)


# ================= ABOUT =================

def about(request):

    return render(request, 'about.html')


# ================= CONTACT =================

def contact(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():

        form.save()

        messages.success(request, "Message Sent")

        return redirect('contact')

    return render(request,
                  'contact.html',
                  {'form': form})


# ================= SHOP =================

def shop(request):

    trains = Train.objects.all()

    return render(request,
                  'shop.html',
                  {'trains': trains})









