
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('values', views.values, name='values'),
    path('awards', views.awards, name='awards'),
    path('vacancy', views.vacancy, name='vacancy'),
    path('application', views.application, name='application'),
]