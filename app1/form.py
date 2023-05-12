from django import forms
from .models import Booking, Contacts

class DatePiker(forms.DateInput):
    input_type = 'Date'

class Booking_form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DatePiker()
        }

        labels = {
        'p_name' : 'Name',
        'P_phone' : 'Phone',
        'P_email' : 'E-mail',
        'doc_name' : 'Doctor',
        'booking_date' : 'Date',
        }

class Contact_form(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'

        labels = {
        'y_name' : 'Name',
        'y_phone' : 'Phone',
        'y_email' : 'E-mail',
        }