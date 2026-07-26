from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('event/', views.event_details, name='event_details'),
    path('rsvp/', views.rsvp, name='rsvp'),
    path('gifts/', views.gifts, name='gifts'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
