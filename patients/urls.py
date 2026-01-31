from django.urls import path
from . import views

urlpatterns = [
    path('', views.patients_list, name='patients_list'),  # Liste des patients
    path('ajouter/', views.patients_create, name='patients_create'),
    path('<int:pk>/modifier/', views.patients_update, name='patients_update'),
    path('<int:pk>/supprimer/', views.patients_delete, name='patients_delete'),
]
