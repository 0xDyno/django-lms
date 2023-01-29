from django.urls import path

from . import views

app_name = "student"

urlpatterns = [
    path("", views.all_students_view, name="all"),
    path("<int:pk>/", views.student_view, name="info"),
    path("create/", views.create_student_view, name="create"),
    path("edit/<int:pk>/", views.edit_student_view, name="edit"),
    path("delete/<int:pk>/", views.delete_student_view, name="delete"),
]
