# Generated by Django 4.1.7 on 2023-04-21 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_studentresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresult',
            old_name='subjecct_id',
            new_name='subject_id',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='pdated_at',
            new_name='updated_at',
        ),
    ]