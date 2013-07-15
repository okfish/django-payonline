from django.conf import settings
from django.core.urlresolvers import reverse


CONFIG = {
    'MERCHANT_ID': None,
    'PRIVATE_SECURITY_KEY': None,
    'PAYONLINE_URL': 'https://secure.payonlinesystem.com/ru/payment/select/',
    'CURRENCY': 'RUB',
    'RETURN_URL':  reverse('payonline_success'),
}

CONFIG.update(getattr(settings, 'PAYONLINE_CONFIG', {}))
