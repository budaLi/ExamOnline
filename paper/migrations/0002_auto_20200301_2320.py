# Generated by Django 3.0.3 on 2020-03-01 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='fill_question',
            new_name='fill_num',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='judge_question',
            new_name='judge_num',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='program_question',
            new_name='program_num',
        ),
    ]
