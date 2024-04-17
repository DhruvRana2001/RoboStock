from django.contrib import admin
from django.urls import path, include

from RoboStockApp import views

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('about us', views.about_us, name='about-us'),
    path("help", views.help, name='help'),
    path("sign in", views.sign_in, name='sign-in'),
    path("sign up", views.sign_up, name='sign-up'),
]