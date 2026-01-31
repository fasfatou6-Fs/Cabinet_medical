Application de Gestion de Cabinet Médical
👥 Équipe de Développement

    Fatoumata Abdoulaye Samaké

    Kadidiatou Niambélé

    Djélika Traoré 

Date : 31 Janvier 2026

Technologies : Django 6.0.1, Python 3.13
📝 Introduction

Ce projet est une application web dédiée à la gestion d'un cabinet médical. L'objectif est de faciliter le suivi des patients et l'automatisation des ordonnances.
🚀 Fonctionnalités Principales

    Gestion des Consultations : Système CRUD complet pour les rendez-vous.

    Génération d'Ordonnances PDF : Documents au format A5 via ReportLab.

    Chatbot Intelligent : Envoi de bilans par e-mail (SMTP Gmail).

    Sécurité des Accès : Authentification pour protéger les données sensibles.

📊 Conception (Diagrammes UML)

3.1 Diagramme de cas d’utilisation

Ce diagramme montre les rôles de l'Administrateur, du Personnel et du Chatbot.

3.2 Diagramme de classes

Représente les relations entre Patients, Médecins, Rendez-vous et Consultations.

3.3 Diagramme de séquence

Illustre le processus technique d’une prise de rendez-vous.

3.4 Diagramme d’activité

Décrit les étapes de saisie et de validation d’une consultation.

🔧 Défis Techniques et Solutions

    Gestion des erreurs : Correction des erreurs AttributeError liées aux dates.

    Compatibilité : Suppression du champ signature inexistant pour les PDF.

    Sécurité : Configuration du "Mot de passe d'application" Google.

📦 Déploiement

    GitHub : Projet nommé cabinet médical.

    Structure : Dossier env exclu pour plus de propreté.

    Maintenance : Fichier requirements.txt inclus.

📈 Perspectives d'Évolution

    Calendrier de prise de rendez-vous en ligne.

    Rappels automatiques par SMS.

    Archivage sécurisé des dossiers complets.
