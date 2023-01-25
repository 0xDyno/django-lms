from django.urls import path

from . import views

urlpatterns = [
    path("students/", views.all_students_view, name="students"),
    path("students/<int:pk>", views.student_view, name="student"),
    path("students/create/", views.create_student_view, name="create"),
    path("students/edit/<int:pk>", views.edit_student_view, name="edit"),
    path("students/delete/<int:pk>", views.delete_student_view, name="delete"),
]
