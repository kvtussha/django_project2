import json

from django.core.management import BaseCommand

from main_app.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        Post.objects.all().delete()

        posts_list = []
        with open('main_app/fixtures/main_app/posts.json', encoding='utf-8') as f:
            posts = json.load(f)
        for post in posts:
            posts_list.append(post["fields"])
        print(posts_list)
        for post in posts_list:
            Post.objects.create(**post)
