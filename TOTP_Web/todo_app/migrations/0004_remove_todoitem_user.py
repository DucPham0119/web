# Generated by Django 3.0.5 on 2023-03-24 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todoitem_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='user',
        ),
    ]