# Generated by Django 3.2.19 on 2023-06-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_useritfess_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.TextField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
