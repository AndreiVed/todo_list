# Generated by Django 5.1.1 on 2024-09-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_app', '0003_alter_task_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
