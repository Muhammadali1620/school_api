from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.StudentRegisterAPIView.as_view(), name='register_student'),
    path('students/<int:pk>/', views.RetrieveStudentAPIView.as_view(), name='retrieve_student'),
    path('students/update/<int:pk>/', views.UpdateStudentAPIView.as_view(), name='update_student'),
    path('students/delete/<int:pk>/', views.DeleteStudentAPIView.as_view(), name='delete_student'),

    path('teachers/', views.TeacherRegisterAPIView.as_view(), name='register_teacher'),
    path('teachers/<int:pk>/', views.RetrieveTeacherAPIVew.as_view(), name='retrieve_teacher'),
    path('teachers/update/<int:pk>/', views.UpdateTeacherAPIVew.as_view(), name='update_teacher'),
    path('teachers/delete/<int:pk>/', views.DeleteTeacherAPIView.as_view(), name='delete_teacher'),
]