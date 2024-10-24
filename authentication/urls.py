from django.urls import path
from .views import (
    homePage,
    logoutView
)

app_name = 'authentication'

urlpatterns = [
    path("", homePage, name='home'),
    path("logout", logoutView, name='logout'),
]