# Generated by Django 3.2.13 on 2022-05-01 12:57

import InvenTree.fields
import InvenTree.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0042_supplierpricebreak_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManufacturerPartAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, help_text='Select file to attach', null=True, upload_to='attachments', verbose_name='Attachment')),
                ('link', InvenTree.fields.InvenTreeURLField(blank=True, help_text='Link to external URL', null=True, verbose_name='Link')),
                ('comment', models.CharField(blank=True, help_text='File comment', max_length=100, verbose_name='Comment')),
                ('upload_date', models.DateField(auto_now_add=True, null=True, verbose_name='upload date')),
                ('manufacturer_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='company.manufacturerpart', verbose_name='Manufacturer Part')),
                ('user', models.ForeignKey(blank=True, help_text='User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
