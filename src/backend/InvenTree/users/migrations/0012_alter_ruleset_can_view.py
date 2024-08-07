# Generated by Django 4.2.12 on 2024-07-18 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_auto_20240523_1640"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ruleset",
            name="can_view",
            field=models.BooleanField(
                default=False, help_text="Permission to view items", verbose_name="View"
            ),
        ),
    ]
