# Generated by Django 4.2.1 on 2023-06-16 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_subject_code_theory_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='theory',
            old_name='code',
            new_name='subject_code',
        ),
        migrations.RenameField(
            model_name='theory',
            old_name='name',
            new_name='teacher_name',
        ),
    ]