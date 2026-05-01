from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        # We check if the user already exists to avoid errors
        username = "admin"  # You can change this
        email = "admin@example.com"
        password = "admin" # Change this!
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Successfully created superuser: {username}'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))