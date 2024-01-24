from django.contrib import admin
from django.urls import path, include
from .views import forecast, index


urlpatterns = [
    path('', index, name="index"),
    path('updates', forecast, name="forecast")

]
