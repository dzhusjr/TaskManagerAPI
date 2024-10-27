import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import User
from projects.models import Project
from tasks.models import Task

class Command(BaseCommand):
    help = 'Import Tasks CSV files to the database'

    def handle(self, *args, **kwargs):
        with open('data/tasks.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Task.objects.create(
                    title=row['title'],
                    description=row['description'],
                    order=row['order'],
                    created_at=row['created_at'],
                )
        self.stdout.write(self.style.SUCCESS('Tasks imported successfully.'))
