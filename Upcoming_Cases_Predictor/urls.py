
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from  . import  views

urlpatterns = [
    path('', views.home,name='home'),
    path('country/', views.country_home, name='country_home'),
    path('country/predict-1/', views.country_predict, name='country_predict'),
    path('state/', views.state_home, name='state_home'),
    path('state/predict-2/', views.state_predict, name='state_predict'),
    path('district/', views.district_home, name='district_home'),
    path('district/predict-3/', views.district_predict, name='district_predict'),
    path('coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
]
