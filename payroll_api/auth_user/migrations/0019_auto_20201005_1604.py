# Generated by Django 3.0.8 on 2020-10-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0018_auto_20200928_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='acknowledgment_approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='acknowledgment_show',
            field=models.BooleanField(default=False),
        ),
    ]
