# Generated by Django 3.2.16 on 2022-11-12 01:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import djmoney.models.validators

import InvenTree.fields
import common.currency
import common.settings

class Migration(migrations.Migration):

    dependencies = [
        ('part', '0088_alter_partparametertemplate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='base_cost',
            field=models.DecimalField(decimal_places=6, default=0, help_text='Minimum charge (e.g. stocking fee)', max_digits=19, validators=[django.core.validators.MinValueValidator(0)], verbose_name='base cost'),
        ),
        migrations.AlterField(
            model_name='partinternalpricebreak',
            name='price',
            field=InvenTree.fields.InvenTreeModelMoneyField(currency_choices=[], decimal_places=6, default_currency='', help_text='Unit price at specified quantity', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='partsellpricebreak',
            name='price',
            field=InvenTree.fields.InvenTreeModelMoneyField(currency_choices=[], decimal_places=6, default_currency='', help_text='Unit price at specified quantity', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Price'),
        ),
        migrations.CreateModel(
            name='PartPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=common.currency.currency_code_mappings(), default=common.currency.currency_code_default, help_text='Currency used to cache pricing calculations', max_length=10, verbose_name='Currency')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Timestamp of last pricing update', verbose_name='Updated')),
                ('scheduled_for_update', models.BooleanField(default=False)),
                ('bom_cost_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('bom_cost_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Minimum cost of component parts', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum BOM Cost')),
                ('bom_cost_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('bom_cost_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Maximum cost of component parts', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum BOM Cost')),
                ('purchase_cost_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('purchase_cost_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Minimum historical purchase cost', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum Purchase Cost')),
                ('purchase_cost_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('purchase_cost_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Maximum historical purchase cost', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum Purchase Cost')),
                ('internal_cost_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('internal_cost_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Minimum cost based on internal price breaks', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum Internal Price')),
                ('internal_cost_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('internal_cost_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Maximum cost based on internal price breaks', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum Internal Price')),
                ('supplier_price_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('supplier_price_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Minimum price of part from external suppliers', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum Supplier Price')),
                ('supplier_price_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('supplier_price_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Maximum price of part from external suppliers', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum Supplier Price')),
                ('variant_cost_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('variant_cost_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Calculated minimum cost of variant parts', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum Variant Cost')),
                ('variant_cost_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('variant_cost_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Calculated maximum cost of variant parts', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum Variant Cost')),
                ('overall_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('overall_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Calculated overall minimum cost', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum Cost')),
                ('overall_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('overall_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Calculated overall maximum cost', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum Cost')),
                ('sale_price_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('sale_price_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Minimum sale price based on price breaks', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum Sale Price')),
                ('sale_price_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('sale_price_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Maximum sale price based on price breaks', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum Sale Price')),
                ('sale_history_min_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('sale_history_min', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Minimum historical sale price', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Minimum Sale Cost')),
                ('sale_history_max_currency', djmoney.models.fields.CurrencyField(choices=[], default='', editable=False, max_length=3)),
                ('sale_history_max', InvenTree.fields.InvenTreeModelMoneyField(blank=True, currency_choices=[], decimal_places=6, default_currency='', help_text='Maximum historical sale price', max_digits=19, null=True, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Maximum Sale Cost')),
                ('part', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pricing_data', to='part.part', verbose_name='Part')),
            ],
        ),
    ]
