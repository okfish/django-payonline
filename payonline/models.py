from django.db import models
from django.utils.translation import ugettext_lazy as _

from .fields.models import UTCDateTimeField

CURRENCIES = (
    ('RUB', _('RUB')),
    ('USD', _('USD')),
    ('EUR', _('EUR')),
)

PROVIDERS = (
    ('Card', _('Card')),
    ('Qiwi', _('Qiwi')),
    ('WebMoney', _('WebMoney')),
)


class PaymentData(models.Model):

    datetime = UTCDateTimeField()
    transaction_id = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCIES)
    provider = models.CharField(max_length=10, choices=PROVIDERS)
    order_id = models.CharField(max_length=50, blank=True)

    card_holder = models.CharField(max_length=255, blank=True)
    card_number = models.CharField(max_length=16, blank=True)
    country = models.CharField(max_length=2, blank=True)
    city = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    wm_tran_id = models.PositiveIntegerField(null=True, blank=True)
    wm_inv_id = models.PositiveIntegerField(null=True, blank=True)
    wm_id = models.CharField(max_length=255, blank=True)
    wm_purse = models.CharField(max_length=255, blank=True)

    ip_address = models.CharField(max_length=255, blank=True)
    ip_country = models.CharField(max_length=2, blank=True)
    bin_country = models.CharField(max_length=2, blank=True)
