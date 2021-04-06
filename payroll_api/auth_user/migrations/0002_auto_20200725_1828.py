# Generated by Django 3.0.8 on 2020-07-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permission',
            old_name='master',
            new_name='master_add',
        ),
        migrations.AddField(
            model_name='permission',
            name='master_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='master_update',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='master_view',
            field=models.BooleanField(default=False),
        ),
    ]