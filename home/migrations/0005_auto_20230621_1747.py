# Generated by Django 3.2.19 on 2023-06-21 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_member_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='member',
            name='nama',
            field=models.CharField(max_length=100),
        ),
    ]
