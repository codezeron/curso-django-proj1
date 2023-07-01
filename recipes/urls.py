from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="recipes-home"),  # /
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
    path('contato/', views.contato, name="recipes-contato"),  # /contato
    path('sobre/', views.sobre, name="recipes-sobre"),  # /sobre
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)