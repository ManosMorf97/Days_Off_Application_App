from django.urls import path
from . import views

urlpatterns=[
    path('welcome/',views.welcome_employee),
    path('welcome2/',views.test)
]