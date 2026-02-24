from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        users = db.users
        teams = db.teams
        activities = db.activities
        leaderboard = db.leaderboard
        workouts = db.workouts

        # Daten löschen
        users.delete_many({})
        teams.delete_many({})
        activities.delete_many({})
        leaderboard.delete_many({})
        workouts.delete_many({})

        # Teams
        marvel = {"name": "Marvel", "members": []}
        dc = {"name": "DC", "members": []}
        teams.insert_many([marvel, dc])

        # Users
        user_data = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
        ]
        users.insert_many(user_data)

        # Activities
        activities.insert_many([
            {"user": "Iron Man", "activity": "Running", "duration": 30},
            {"user": "Batman", "activity": "Cycling", "duration": 45},
        ])

        # Leaderboard
        leaderboard.insert_many([
            {"team": "Marvel", "points": 100},
            {"team": "DC", "points": 90},
        ])

        # Workouts
        workouts.insert_many([
            {"user": "Wonder Woman", "workout": "Yoga", "duration": 60},
            {"user": "Captain America", "workout": "HIIT", "duration": 40},
        ])

        # Unique Index für Email
        users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db erfolgreich mit Testdaten befüllt!'))
