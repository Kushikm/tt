# Generated by Django 4.2 on 2023-06-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_instructor'),
    ]

    operations = [
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('sem', models.CharField(max_length=50)),
            ],
        ),
    ]