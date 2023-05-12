from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home),
    path('About/', views.About),
    path('Booking/', views.Booking),
    path('Contact/', views.Contact),
    path('Department/', views.Departmentzzz),
    path('Doctors/', views.Doctorsss),
    # path('Booking_post/', views.Booking_post)
]