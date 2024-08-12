from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("product_list/", views.ProductView.as_view(), name="list"),
    path("create/", views.ProductCreateView.as_view(), name="create"),
    path("update/<int:pk>/", views.ProductUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", views.ProductDeleteView.as_view(), name="delete"),
    path("details/<int:id>/", views.ProductDetailsView.as_view(), name="details"),
    path("search/", views.SearchProductView.as_view(), name="search"),
]
