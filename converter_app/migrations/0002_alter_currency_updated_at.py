# Generated by Django 4.1.7 on 2023-05-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]