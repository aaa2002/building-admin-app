# Generated by Django 5.0.1 on 2024-01-06 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_admin_user_profile_alter_buyer_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.apartmentbuilding'),
        ),
        migrations.DeleteModel(
            name='ApartmentBuildingPlace',
        ),
    ]
