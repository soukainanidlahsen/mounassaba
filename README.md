# Mounassaba — Marketplace événementielle au Maroc

Mounassaba est une plateforme web qui met en relation les particuliers souhaitant organiser des événements au Maroc avec des prestataires professionnels (photographes, traiteurs, décorateurs, DJ, etc.).

## Architecture

```
mounassaba/
├── backend/     # Django 5 + Django REST Framework (API)
├── frontend/    # React 18 + Vite (SPA)
└── README.md
```

## Prérequis

- Python 3.12+
- Node.js 20+
- npm 10+
- Git

## Installation

### Backend

```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_data  # Données de démonstration
python manage.py runserver
```

Le serveur API démarre sur `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

Le serveur de développement démarre sur `http://localhost:5173`.

## Comptes de démonstration

*(Seront ajoutés après la Phase 3)*

## Technologies

| Composant | Technologie |
|-----------|-------------|
| Backend | Django 5, Django REST Framework, SimpleJWT |
| Frontend | React 18, Vite, React Router, Axios |
| Base de données | SQLite (dev) / PostgreSQL (prod) |
| Authentification | JWT (Access + Refresh tokens) |

## Licence

Projet privé — Tous droits réservés.
