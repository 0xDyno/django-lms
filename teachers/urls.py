from django.urls import path

from . import views


urlpatterns = [
    path("", views.all_teachers_view, name="teachers"),
    path("<int:pk>/", views.teacher_view, name="teacher"),
    path("create/", views.create_teacher_view, name="create_teacher"),
    path("edit/<int:pk>/", views.edit_teacher_view, name="edit_teacher"),
    path("delete/<int:pk>/", views.delete_teacher_view, name="delete_teacher"),
]