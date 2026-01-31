from django.urls import path
from . import views

urlpatterns = [
    path('', views.medecins_list, name='medecins_list'),
    path('ajouter/', views.medecins_create, name='medecins_create'),
    path('<int:pk>/modifier/', views.medecins_update, name='medecins_update'),
    path('<int:pk>/supprimer/', views.medecins_delete, name='medecins_delete'),
]
