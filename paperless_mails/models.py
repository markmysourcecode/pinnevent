from django.db import models
from django.utils.translation import ugettext_lazy as _



# email subscriber
class EmailSubscriber(models.Model):
    email = models.EmailField(_('email address'), unique=True)
    subscribe_at = models.DateTimeField(auto_now_add=True)
    unsubscribe_at = models.DateTimeField(null=True, blank=True)
    is_subscriber = models.BooleanField(default=True)