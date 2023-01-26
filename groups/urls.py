from django.urls import path

from . import views


urlpatterns = [
    path("", views.all_groups_view, name="groups"),
    path("<int:pk>/", views.group_view, name="group"),
    path("create/", views.create_group_view, name="create_group"),
    path("edit/<int:pk>/", views.edit_group_view, name="edit_group"),
    path("delete/<int:pk>/", views.delete_group_view, name="delete_group"),
]
