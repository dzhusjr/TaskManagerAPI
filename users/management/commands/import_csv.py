import csv
from django.core.management.base import BaseCommand
from users.models import User
from projects.models import Project
from tasks.models import Task

class Command(BaseCommand):
    help = 'Import CSV files to the database'

    def handle(self, *args, **kwargs):
        with open('data/users.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                User.objects.create(
                    first_name=row['name'].split(' ')[0],
                    last_name=row['name'].split(' ')[1],
                    username=row['name'].replace(' ', '_'),
                    email=row['email'],
                    password=row['password']
                )
        with open('data/projects.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Project.objects.create(
                    title=row['title'],
                    description=row['description'],
                    order=row['order']
                )
        with open('data/tasks.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Task.objects.create(
                    title=row['title'],
                    description=row['description'],
                    order=row['order'],
                    created_at=row['created_at'],
                )
        # Repeat for projects and tasks
        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
