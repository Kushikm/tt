# Generated by Django 4.2.1 on 2023-06-16 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_theory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theory',
            name='subject_name',
        ),
        migrations.RemoveField(
            model_name='theory',
            name='teacher_designation',
        ),
        migrations.RemoveField(
            model_name='theory',
            name='teacher_id',
        ),
    ]
