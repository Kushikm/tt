# Generated by Django 4.2 on 2023-06-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_subjects_credits_alter_instructor_designation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
