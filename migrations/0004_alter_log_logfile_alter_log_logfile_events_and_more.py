# Generated by Django 4.0.10 on 2023-05-08 20:03

import ProcessAdminRestApi.models.fields.XLSX_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic_app', '0003_log_rename_frontendid_userchangelog_calculationid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='logfile',
            field=ProcessAdminRestApi.models.fields.XLSX_field.XLSXField(default='', max_length=300, upload_to=''),
        ),
        migrations.AlterField(
            model_name='log',
            name='logfile_events',
            field=ProcessAdminRestApi.models.fields.XLSX_field.XLSXField(default='', max_length=300, upload_to=''),
        ),
        migrations.AlterField(
            model_name='log',
            name='logfile_timesheet',
            field=ProcessAdminRestApi.models.fields.XLSX_field.XLSXField(default='', max_length=300, upload_to=''),
        ),
    ]
