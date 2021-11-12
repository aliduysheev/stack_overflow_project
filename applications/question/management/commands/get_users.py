from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from datetime import datetime


class Command(BaseCommand):
    help = 'Displays all users'

    def handle(self, *args, **kwargs):
       users = get_user_model().objects.all()
       for user in users:
            self.stdout.write(f'Username {user.email}')