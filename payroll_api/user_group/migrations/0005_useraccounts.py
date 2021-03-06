# Generated by Django 3.0.8 on 2020-07-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_group', '0004_usergroup_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('active', models.BooleanField(default=True)),
                ('last_login', models.DateField(blank=True, null=True)),
                ('created', models.DateField(auto_now=True)),
            ],
        ),
    ]
