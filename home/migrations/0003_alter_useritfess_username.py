# Generated by Django 3.2.19 on 2023-06-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230601_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useritfess',
            name='username',
            field=models.CharField(max_length=254),
        ),
    ]
