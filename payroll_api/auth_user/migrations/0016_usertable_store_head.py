# Generated by Django 3.0.8 on 2020-09-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0015_usertable_notification_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='store_head',
            field=models.BooleanField(default=False),
        ),
    ]