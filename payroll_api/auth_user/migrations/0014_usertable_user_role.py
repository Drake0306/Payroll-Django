# Generated by Django 3.0.8 on 2020-09-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0013_auto_20200925_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='user_role',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]