from django.urls import path
from . import views

urlpatterns = [
    path('', views.resumen, name='inicio'),
    path('resumen/', views.resumen, name='resumen'),
]