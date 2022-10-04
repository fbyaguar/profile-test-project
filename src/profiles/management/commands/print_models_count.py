from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    def handle(self, *args, **options):
        app_models = apps.get_models()
        for app_model in app_models:
            self.stdout.write(f'{app_model.__name__}: {app_model.objects.count()}')
