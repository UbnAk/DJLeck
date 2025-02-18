# Для удаления объектов модели можно использовать методы delete()
# экземпляра класса модели. Если надо удалить пользователя, мы можем
# использовать следующий код в файле
# myapp2/management/commands/delete_user.py:
from django.core.management.base import BaseCommand
from myapp2.models import User

class Command(BaseCommand):
    help = "Delete user by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')