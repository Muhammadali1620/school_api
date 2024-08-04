from django.urls import path
from . import views


urlpatterns = [
    path('', views.SubjectListCreateAPIView.as_view(), name='subjects'),
]