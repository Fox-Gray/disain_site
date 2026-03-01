from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='kulkulatori'),
    path('shirka/', views.calcshirka, name='shirka'),
]