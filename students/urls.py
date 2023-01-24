from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("students/", views.all_students_view, name="students"),
    path("students/<int:pk>", views.student_view, name="student"),
    path("students/create/", views.create_student_view, name="create"),
    path("students/delete/<int:pk>", views.delete_student_view, name="delete"),
]
