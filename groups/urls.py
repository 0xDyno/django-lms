from django.urls import path

from . import views

app_name = "group"

urlpatterns = [
    path("", views.all_groups_view, name="all"),
    path("<int:pk>/", views.group_view, name="info"),
    path("create/", views.create_group_view, name="create"),
    path("edit/<int:pk>/", views.edit_group_view, name="edit"),
    path("delete/<int:pk>/", views.delete_group_view, name="delete"),
]
