# Generated by Django 4.2.11 on 2024-04-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_app', '0004_rename_good_mailfiles_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailfiles',
            name='file_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='mailfiles',
            unique_together={('file', 'mail')},
        ),
    ]
