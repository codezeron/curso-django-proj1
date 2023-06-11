from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),  # /
    path('recipes/<int:id>/', views.recipe),
    path('contato/', views.contato),  # /contato
    path('sobre/', views.sobre),  # /sobre
]