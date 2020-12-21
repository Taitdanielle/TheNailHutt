from django.urls import path
from . import views

urlpatterns = [
    path('', views.parties, name='parties'),
    path('success/', views.parties_thankyou, name='parties_thankyou'),
]