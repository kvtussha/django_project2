import json

from django.core.management import BaseCommand

from main_app.models import CategoryModel


class Command(BaseCommand):

    def handle(self, *args, **options):
        CategoryModel.objects.all().delete()

        categories_list = []
        with open('main_app/fixtures/main_app/categories.json', encoding='utf-8') as f:
            categories = json.load(f)

        for category_item in categories:
            if len(categories_list):
                categories_list.append(category_item["fields"])
        print(categories_list)

        for category_item in categories_list:
            CategoryModel.objects.create(**category_item)
