# Generated by Django 5.0.1 on 2024-01-06 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_userprofile_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('imgUrl', models.CharField(max_length=255)),
                ('post_date', models.DateField()),
                ('price', models.FloatField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.apartment')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.admin')),
            ],
        ),
    ]
