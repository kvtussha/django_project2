from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Настройка групп загрузки для ролей модератора'

    def handle(self, *args, **options):
        call_command('loaddata', 'groups_fixture.json')
