# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("data/<int:pk>/", views.get_data),
    path("data/", views.create_data),
    path("update/<int:pk>/", views.update_data),
    path("delete/<int:pk>/", views.delete_data),
]
