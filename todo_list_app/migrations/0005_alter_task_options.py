# Generated by Django 5.1.1 on 2024-09-30 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0004_alter_task_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_date']},
        ),
    ]
