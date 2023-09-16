from django.urls import path
from . import views

urlpatterns=[
    path('welcome_manager/',views.welcome_manager),
    path('answer_requests/',views.answer_requests)
]