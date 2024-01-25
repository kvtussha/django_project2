# Generated by Django 5.0 on 2024-01-25 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_client_mailing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailingmessage',
            name='mailing',
        ),
        migrations.AddField(
            model_name='mailing',
            name='mailing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='main_app.mailingmessage', verbose_name='Mailing message'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='mailing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mailings', to='main_app.mailingmessage', verbose_name='Mailing time'),
        ),
        migrations.AlterField(
            model_name='mailinglog',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='main_app.mailingmessage', verbose_name='Mailing time'),
        ),
    ]
