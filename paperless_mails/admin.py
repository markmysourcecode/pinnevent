from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from paperless_mails.models import EmailSubscriber


@admin.register(EmailSubscriber)
class EmailSubscriberAdmin(admin.ModelAdmin):
    fields = ('email', 'subscribe_at', 'unsubscribe_at', 'is_subscriber')
    readonly_fields = ('subscribe_at', 'unsubscribe_at',)