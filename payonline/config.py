from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PayonlineConfig(AppConfig):
    label = 'payonline'
    name = 'payonline'
    verbose_name = _('PayOnline')
