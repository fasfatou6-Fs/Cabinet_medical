from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultations_list, name='consultations_list'),
    path('ajouter/', views.consultations_create, name='consultations_create'),
    path('<int:pk>/modifier/', views.consultations_update, name='consultations_update'),
    path('<int:pk>/supprimer/', views.consultations_delete, name='consultations_delete'),
    
    # Ligne pour le chatbot
    path('chat-api/', views.get_bot_response, name='get_bot_response'),

    # --- NOUVELLE LIGNE POUR LE PDF ---
    path('<int:pk>/ordonnance/', views.generer_ordonnance_pdf, name='generer_ordonnance_pdf'),
]