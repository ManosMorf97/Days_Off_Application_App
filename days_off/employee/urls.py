from django.urls import path
from . import views

urlpatterns=[
    path('welcome/',views.welcome_employee),
    path('welcome2/',views.test),
    path('new_request/',views.request_days),
    path('left_days_off/',views.left_days_off),
    path('decisions/',views.decisions)
]