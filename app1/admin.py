from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Doctors)

class admin_view(admin.ModelAdmin):
     list_display = ('id','p_name','P_phone','P_email','doc_name','booking_date')
admin.site.register(Booking,admin_view)

class admin_view_contact(admin.ModelAdmin):
     list_display = ('id','y_name','y_phone','y_email')
admin.site.register(Contacts,admin_view_contact)