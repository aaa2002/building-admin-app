# Generated by Django 5.0.1 on 2024-01-07 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
