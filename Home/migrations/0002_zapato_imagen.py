# Generated by Django 5.2 on 2025-05-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapato',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='zapatos/'),
        ),
    ]
