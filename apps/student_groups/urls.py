from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.ListCreateStudentGroupAPIView.as_view(), name='add_student_groups'),
    path('<int:pk>/remove/', views.DeleteStudentUpdateGroupAPIView.as_view(), name='remove_student_groups'),
]