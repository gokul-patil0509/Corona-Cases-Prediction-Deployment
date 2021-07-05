
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Upcoming_Cases_Predictor.urls')),
]
