# Generated by Django 5.1.2 on 2024-10-21 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_box', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='message',
        ),
    ]
