# Generated by Django 3.2.dev20201030110133 on 2020-11-17 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ads',
            new_name='Ad',
        ),
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name_plural': 'Ads'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.RenameField(
            model_name='ad',
            old_name='ads_path',
            new_name='ad_path',
        ),
    ]
