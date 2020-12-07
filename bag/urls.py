from django.urls import path
from . import views

urlpatterns = [
    path('', views.views_bag, name='view_bag')
]