# Generated by Django 3.0.8 on 2020-09-26 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0014_usertable_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='notification_new',
            field=models.BooleanField(default=False),
        ),
    ]
