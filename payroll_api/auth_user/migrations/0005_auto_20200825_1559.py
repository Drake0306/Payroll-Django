# Generated by Django 3.0.8 on 2020-08-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0004_auto_20200725_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='grn_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='grn_edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='grn_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='job_card_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='job_card_edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='job_card_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='pending_request_approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='pending_request_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='pending_request_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='premitive_maintaince_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='premitive_maintaince_edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='premitive_maintaince_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='purchase_order_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='purchase_order_approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='purchase_order_edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='purchase_order_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='quality_check_approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='quality_check_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_current_stock_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_grn_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_job_card_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_preventive_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_purchase_order_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_request_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_stock_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='report_storeissue_voucher_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='request_add',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='request_edit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='request_list',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='request_view',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='store_issue_voucher_approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='permission',
            name='store_issue_voucher_view',
            field=models.BooleanField(default=False),
        ),
    ]
