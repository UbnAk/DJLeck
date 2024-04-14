from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Create user."
    
    def handle(self, *args, **kwargs):
        # user = User(name='John', email='john@example.com',
        # password='secret', age=25) #Создаем пользователя
#         user = User(name='Neo', email='neo@example.com', password='secret',
# age=58)
        user = User(name='Maksim', email='maks@example.com', password='secret',
        age=27)
        user.save() #Сохраняем
        self.stdout.write(f'{user}')
        
    
