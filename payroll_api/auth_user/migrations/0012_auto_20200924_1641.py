# Generated by Django 3.0.8 on 2020-09-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0011_auto_20200924_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='branch',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='department',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]