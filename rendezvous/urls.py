from django.urls import path
from . import views

urlpatterns = [
    path('', views.rendezvous_list, name='rendezvous_list'),
    path('ajouter/', views.rendezvous_create, name='rendezvous_create'),
    path('supprimer/<int:pk>/', views.rendezvous_delete, name='rendezvous_delete'),
    path('modifier/<int:pk>/', views.rendezvous_update, name='rendezvous_update'),
]