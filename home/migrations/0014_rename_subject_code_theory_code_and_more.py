# Generated by Django 4.2.1 on 2023-06-16 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_theory_subject_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theory',
            old_name='subject_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='theory',
            old_name='teacher_name',
            new_name='name',
        ),
    ]
