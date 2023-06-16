from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="recipes-home"),  # /
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    path('contato/', views.contato, name="recipes-contato"),  # /contato
    path('sobre/', views.sobre, name="recipes-sobre"),  # /sobre
]