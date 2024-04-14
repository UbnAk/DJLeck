# А чтобы получить пользователя по его ID, мы можем использовать следующий
# код в файле myapp2/management/commands/get_user.py:
# from django.core.management.base import BaseCommand
# from myapp2.models import User
# class Command(BaseCommand):
    
#     help = "Get user by id."
    
#     def add_arguments(self, parser):
#         parser.add_argument('id', type=int, help='User ID')

#     def handle(self, *args, **kwargs):
#         id = kwargs['id']
#         user = User.objects.get(id=id)
#         self.stdout.write(f'{user}')


# Если мы запустим прошлый пример с несуществующим в БД
# идентификатором, получим ошибку: myapp2.models.User.DoesNotExist: User
# matching query does not exist.
# Исправим наш код:
from django.core.management.base import BaseCommand
from myapp2.models import User
class Command(BaseCommand):
    help = "Get user by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
