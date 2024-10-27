import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import User
from projects.models import Project
from tasks.models import Task

class Command(BaseCommand):
    help = 'Import Projects CSV files to the database'

    def handle(self, *args, **kwargs):
        with open('data/projects.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Project.objects.create(
                    title=row['title'],
                    description=row['description'],
                    order=row['order']
                )
        self.stdout.write(self.style.SUCCESS('Projects imported successfully.'))
