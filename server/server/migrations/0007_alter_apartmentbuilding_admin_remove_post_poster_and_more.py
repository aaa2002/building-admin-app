# Generated by Django 5.0.1 on 2024-01-08 04:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_alter_apartment_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentbuilding',
            name='admin',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='post',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='buyer',
            name='user_profile',
        ),
        migrations.RemoveField(
            model_name='post',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='address',
        ),
        migrations.AddField(
            model_name='apartment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='appartment_images'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='price',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='apartmentbuilding',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='apartmentbuilding',
            name='lng',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='area',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='apartmentbuilding',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='apartmentbuilding',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
