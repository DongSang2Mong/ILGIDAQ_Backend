# Generated by Django 3.1.5 on 2021-01-18 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='updated_on',
            new_name='updated_at',
        ),
    ]
