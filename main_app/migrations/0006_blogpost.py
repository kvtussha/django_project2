# Generated by Django 5.0 on 2024-01-17 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_categorymodel_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='название')),
                ('slug', models.TextField(verbose_name='slug')),
                ('content', models.TextField(verbose_name='контент')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('creation_date', models.DateField(verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='статус публикации')),
                ('views_number', models.IntegerField(verbose_name='кол-во просмотров')),
            ],
            options={
                'verbose_name': 'сообщение блога',
                'verbose_name_plural': 'сообщения блога',
                'ordering': ('title',),
            },
        ),
    ]
