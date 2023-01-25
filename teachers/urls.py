from django.urls import path

from . import views


urlpatterns = [
    path("teachers/", views.all_teachers_view, name="teachers"),
    path("teachers/<int:pk>/", views.teacher_view, name="teacher"),
    path("teachers/create/", views.create_teacher_view, name="create_teacher"),
    path("teachers/edit/<int:pk>/", views.edit_teacher_view, name="edit_teacher"),
    path("teachers/delete/<int:pk>/", views.delete_teacher_view, name="delete_teacher"),
]