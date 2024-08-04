from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.AttendanceCreateAPIVew.as_view(), name='attendance'),
]