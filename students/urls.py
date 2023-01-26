from django.urls import path

from . import views


urlpatterns = [
    path("", views.all_students_view, name="students"),
    path("<int:pk>/", views.student_view, name="student"),
    path("create/", views.create_student_view, name="create_student"),
    path("edit/<int:pk>/", views.edit_student_view, name="edit_student"),
    path("delete/<int:pk>/", views.delete_student_view, name="delete_student"),
]
