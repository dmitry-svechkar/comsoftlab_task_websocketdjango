# Generated by Django 4.2.11 on 2024-04-25 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_app', '0003_mail_mail_from'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailfiles',
            old_name='good',
            new_name='mail',
        ),
    ]