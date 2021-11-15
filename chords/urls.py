from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/user/<username>/', views.api_user),
]