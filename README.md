### Projet : Clone de Spotify en Python avec Flask

#### Introduction

Ce projet consiste à créer une version simplifiée de Spotify en utilisant Python et le framework web Flask. L'objectif est de recréer les fonctionnalités de base d'une plateforme de streaming musical, incluant l'authentification des utilisateurs, la gestion des playlists, et le streaming de musique. Ce clone de Spotify permet aux utilisateurs de s'inscrire, de se connecter, de créer des playlists, et d'ajouter des morceaux à ces playlists.

#### Fonctionnalités Principales

1. **Authentification des Utilisateurs** :
   - **Inscription** : Les utilisateurs peuvent s'inscrire en fournissant un nom d'utilisateur et un mot de passe.
   - **Connexion** : Les utilisateurs peuvent se connecter en utilisant leurs identifiants.

2. **Gestion des Utilisateurs** :
   - Les informations des utilisateurs, y compris leurs playlists, sont stockées dans une base de données SQLite.

3. **Streaming de Musique** :
   - Les utilisateurs peuvent accéder à une liste de morceaux de musique disponibles.

4. **Création et Gestion de Playlists** :
   - Les utilisateurs peuvent créer de nouvelles playlists.
   - Les utilisateurs peuvent ajouter des morceaux à leurs playlists.

#### Architecture du Projet

Le projet est structuré en plusieurs fichiers pour une meilleure organisation et maintenabilité :

- **`app.py`** : Point d'entrée de l'application Flask. Initialise l'application, configure la base de données, et enregistre les routes.
- **`config.py`** : Contient la configuration de la base de données SQLite.
- **`models.py`** : Définit les modèles de données pour les utilisateurs, les morceaux de musique, et les playlists.
- **`routes.py`** : Contient les routes API pour l'authentification, la gestion des utilisateurs, et la gestion des playlists.

#### Installation et Exécution

Pour installer et exécuter ce projet, suivez ces étapes :

1. **Cloner le dépôt** :
   ```bash
   git clone <URL_du_dépôt>
   cd spotify_clone
   ```

2. **Installer les dépendances** :
   ```bash
   pip install Flask flask_sqlalchemy
   ```

3. **Exécuter l'application** :
   ```bash
   python app.py
   ```

L'application sera disponible à l'adresse `http://127.0.0.1:5000/`.

#### Endpoints API

- **POST /api/register** : Inscrire un nouvel utilisateur.
  - Exemple de corps de la requête :
    ```json
    {
      "username": "nouvel_utilisateur",
      "password": "mot_de_passe"
    }
    ```

- **POST /api/login** : Connecter un utilisateur.
  - Exemple de corps de la requête :
    ```json
    {
      "username": "nouvel_utilisateur",
      "password": "mot_de_passe"
    }
    ```

- **GET /api/songs** : Obtenir la liste des morceaux de musique disponibles.

- **POST /api/playlists** : Créer une nouvelle playlist pour un utilisateur.
  - Exemple de corps de la requête :
    ```json
    {
      "user_id": 1,
      "name": "Ma nouvelle playlist"
    }
    ```

- **POST /api/playlists/<int:playlist_id>/songs** : Ajouter un morceau à une playlist.
  - Exemple de corps de la requête :
    ```json
    {
      "song_id": 1
    }
    ```

#### Conclusion

Ce projet fournit une base solide pour une application de streaming musical similaire à Spotify. Il peut être étendu avec des fonctionnalités supplémentaires telles que la recherche de morceaux, la lecture de musique en continu, et une interface utilisateur web. Ce clone de Spotify est un excellent exercice pour comprendre comment construire une application web avec Flask et gérer des données utilisateur de manière sécurisée.
