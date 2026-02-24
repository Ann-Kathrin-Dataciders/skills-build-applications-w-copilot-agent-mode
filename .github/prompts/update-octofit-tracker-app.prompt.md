mode: 'agent'
model: GPT-4.1

# Django App Updates

- Alle Django-Projektdateien befinden sich im Verzeichnis `octofit-tracker/backend/octofit_tracker`.

1. Aktualisiere `settings.py` für MongoDB-Verbindung und CORS.
2. Aktualisiere `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py` und `admin.py` zur Unterstützung der Collections users, teams, activities, leaderboard und workouts.
3. Stelle sicher, dass `/` auf die API zeigt und `api_root` in `urls.py` vorhanden ist.
