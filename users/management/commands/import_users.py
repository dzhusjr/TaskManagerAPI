import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from users.models import User
from projects.models import Project
from tasks.models import Task

class Command(BaseCommand):
    help = 'Import Users CSV files to the database'

    def handle(self, *args, **kwargs):
        with open('data/users.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                User.objects.create(
                    first_name=row['name'].split(' ')[0],
                    last_name=row['name'].split(' ')[1],
                    username=row['name'].replace(' ', '_'),
                    email=row['email'],
                    password=make_password(row['password'])
                )
        
        self.stdout.write(self.style.SUCCESS('Users imported successfully.'))
