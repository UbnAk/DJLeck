from django.shortcuts import render
import logging

# Create your views here.
from django.http import HttpResponse

logger = logging.getLogger(__name__)
# Задание №6
# � Добавьте логирование в проект.
# � Настройте возможность вывода в файл и в терминал.
# � Устраните возможные ошибки.
# � *Форматирование настройте по своему желанию.
# Объясните что вы выводите в логи

def index(request):
 logger.info('Index page accessed')
 return HttpResponse("Hello, world!")

def about(request):
    try:
 #  ome code that might raise an exception
        result = 1 / 0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse("Oops, something went wrong.")
    else:
        logger.debug('About page accessed')
        return HttpResponse("This is the about page.")