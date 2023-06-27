# Generated by Django 4.2.1 on 2023-06-16 13:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_rename_code_theory_subject_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='theory',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.instructor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theory',
            name='subject',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='home.subjects'),
            preserve_default=False,
        ),
    ]