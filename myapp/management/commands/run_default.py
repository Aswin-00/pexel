from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core.management import call_command

from decouple import config

class Command(BaseCommand):
    help = 'Add social providers to the database'
    

    def handle(self, *args, **kwargs):
        username =config('PAGE_ADMIN_USERNAME')
        email = config('PAGE_ADMIN_EMAIL')
        password = config('PAGE_ADMIN_PASSWORD')

        
         # set all database 
        call_command('collectstatic')
        call_command('makemigrations')
        call_command('migrate')
        
        
            
           
        
        if not User.objects.filter(username=username).exists():
            
            # create superuser 
            call_command('createsuperuser', username=username, email=email, interactive=False)
            
            # Set the password
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            # collectstatic

            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully with password!'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists.'))
            
            

        
        
        