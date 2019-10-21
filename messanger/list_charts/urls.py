from django.urls import path, include
from . import views

urlpatterns = [
    path('chart/', include("chart.urls")),
    path('', views.index),
]
