from django.urls import path

from . import views

app_name = "teacher"

urlpatterns = [
    path("", views.all_teachers_view, name="all"),
    path("<int:pk>/", views.teacher_view, name="info"),
    path("create/", views.create_teacher_view, name="create"),
    path("edit/<int:pk>/", views.edit_teacher_view, name="edit"),
    path("delete/<int:pk>/", views.delete_teacher_view, name="delete"),
]
