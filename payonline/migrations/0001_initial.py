# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import payonline.fields.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', payonline.fields.models.UTCDateTimeField()),
                ('transaction_id', models.PositiveIntegerField()),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2)),
                ('currency', models.CharField(max_length=3, choices=[(b'RUB', 'RUB'), (b'USD', 'USD'), (b'EUR', 'EUR')])),
                ('provider', models.CharField(max_length=10, choices=[(b'Card', 'Card'), (b'Qiwi', 'Qiwi'), (b'WebMoney', 'WebMoney')])),
                ('order_id', models.CharField(max_length=50, blank=True)),
                ('card_holder', models.CharField(max_length=255, blank=True)),
                ('card_number', models.CharField(max_length=16, blank=True)),
                ('country', models.CharField(max_length=2, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('address', models.CharField(max_length=255, blank=True)),
                ('phone', models.CharField(max_length=255, blank=True)),
                ('wm_tran_id', models.PositiveIntegerField(null=True, blank=True)),
                ('wm_inv_id', models.PositiveIntegerField(null=True, blank=True)),
                ('wm_id', models.CharField(max_length=255, blank=True)),
                ('wm_purse', models.CharField(max_length=255, blank=True)),
                ('ip_address', models.CharField(max_length=255, blank=True)),
                ('ip_country', models.CharField(max_length=2, blank=True)),
                ('bin_country', models.CharField(max_length=2, blank=True)),
            ],
        ),
    ]
