# Generated by Django 3.0.7 on 2021-02-18 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0004_auto_20210210_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='pincode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_name', models.CharField(max_length=250)),
                ('pin_code', models.CharField(max_length=250)),
                ('district', models.CharField(max_length=250)),
                ('state_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='UMO',
        ),
    ]
