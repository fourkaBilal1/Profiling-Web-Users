# Generated by Django 3.2.dev20201030110133 on 2021-01-10 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_search_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_input',
            name='date_search',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date_search'),
            preserve_default=False,
        ),
    ]