from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name = 'index'),
    path('profile/', Profiles, name = 'profile'),
    path('view/', GetProfiles, name = 'view'),
    path('delete/<int:id>', DeleteProfile, name='delete'),
    path('search/', SearchProfile, name='search'),
    path('readprofile/<str:id>', ReadProfile, name='readprofile'),
]
