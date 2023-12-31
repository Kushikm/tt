# Generated by Django 4.2.1 on 2023-06-15 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_instructor_designation_alter_subjects_credits_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('teacher_id', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=100)),
                ('teacher_designation', models.CharField(max_length=100)),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
    ]
