# Generated by Django 4.1.7 on 2023-05-15 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter_app', '0002_alter_currency_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converter',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
