from django.shortcuts import render
from django.http import  HttpResponse
from .models import *
from .form import Booking_form, Contact_form

# Create your views here.
def Home(request):
    return  render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')

def Booking(request):
    if request.method == 'POST':
        form1 = Booking_form(request.POST)
        if form1.is_valid():
            form1.save()
            # return render(request, "booked_alert.html")
    ab = Booking_form()
    fr = ab
    return render(request, "Booking.html", {'data':fr})

def Contact(request):
    if request.method == 'POST':
        form2 = Contact_form(request.POST)
        if form2.is_valid():
            form2.save()
    abcd = Contact_form()
    frc = abcd
    return render(request, 'Contact.html', {'data':frc})

def Departmentzzz(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request, 'Department.html', dict_dept)

def Doctorsss(request):
    get_doc = Doctors.objects.all()
    return render(request, 'Doctors.html', {'data':get_doc})