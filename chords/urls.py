from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/combinations/<int:combination_id>/', views.api_combinations_get),
    path('api/combinations/', views.api_combinations_post)
]