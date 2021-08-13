
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('app/', include('Upcoming_Cases_Predictor.urls')),
]
