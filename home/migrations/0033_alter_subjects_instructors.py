# Generated by Django 4.2.1 on 2023-06-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_subjects_instructors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='instructors',
            field=models.ManyToManyField(max_length=100, to='home.instructor'),
        ),
    ]
