# Generated by Django 4.2.1 on 2023-06-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_department_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='courses',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='department',
            name='depname',
            field=models.CharField(max_length=30),
        ),
    ]
