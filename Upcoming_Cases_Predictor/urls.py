
from django.urls import include, path
from django.conf.urls import url
from django.conf import settings
from  . import  views

urlpatterns = [
    path('', views.home,name='home'),
    path('coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
    path('country/', views.country_home, name='country_home'),
    path('country/predict-1/', views.country_predict, name='country_predict'),
    path('country/coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('country/coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
    path('country/predict-1/coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('country/predict-1/coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
    path('state/', views.state_home, name='state_home'),
    path('state/predict-2/', views.state_predict, name='state_predict'),
    path('state/coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('state/coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
    path('state/predict-2/coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('state/predict-2/coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
    path('district/', views.district_home, name='district_home'),
    path('district/predict-3/', views.district_predict, name='district_predict'),
    path('district/coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('district/coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
    path('district/predict-3/coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('district/predict-3/coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
    path('faqs/', views.faq, name='faq'),
    path('faqs/coronavirus/', views.coronavirus_home, name='coronavirus_home'),
    path('faqs/coronavirus/predict-4/', views.coronavirus_predict, name='coronavirus_predict'),
]
