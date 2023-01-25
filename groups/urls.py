from django.urls import path

from . import views


urlpatterns = [
    path("groups/", views.all_groups_view, name="groups"),
    path("groups/<int:pk>/", views.group_view, name="group"),
    path("groups/create/", views.create_group_view, name="create_group"),
    path("groups/edit/<int:pk>/", views.edit_group_view, name="edit_group"),
    path("groups/delete/<int:pk>/", views.delete_group_view, name="delete_group"),
]
