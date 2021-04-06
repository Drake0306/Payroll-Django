# Generated by Django 3.0.8 on 2020-09-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0010_auto_20200924_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertable',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertable',
            name='grn_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='grn_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='job_card_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='job_card_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='master_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='master_edit',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='master_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='master_status',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='mis_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='preventive_main_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='preventive_main_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='purchase_enquiry_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='purchase_enquiry_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='purchase_order_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='purchase_order_approval',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='purchase_order_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='quality_check',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='quality_check_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='reports_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='request_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='request_approval',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='request_approval_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='request_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='settings_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='settings_edit',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='settings_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='settings_status_change',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='store_issue_voucher_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='store_issue_voucher_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usertable',
            name='transfer_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='transfer_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='work_order_add',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usertable',
            name='work_order_show',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
