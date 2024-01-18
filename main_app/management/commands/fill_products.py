import json

from django.core.management import BaseCommand

from main_app.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()

        products_list = []
        with open('main_app/fixtures/main_app/products.json', encoding='utf-8') as f:
            products = json.load(f)
        for product_item in products:
            products_list.append(product_item["fields"])
        print(products_list)
        for product_item in products_list:
            Product.objects.create(**product_item)
