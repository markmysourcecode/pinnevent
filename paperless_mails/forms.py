from django import forms
from paperless_mails.models import EmailSubscriber
from django.core.exceptions import ValidationError
from application_events import application_functions as aef


class EmailSubscriberForm(forms.ModelForm):
    subscriber_email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-sm',
                'aria-describedby': 'emailHelp',
                'placeholder': 'your email address',
            }),
        error_messages={
            'required': 'let\'s have your email address so we can reserve you the party!',
            'invalid': 'We appreciate it, but we need you to provide a valid email address.',
            }
        )

    class Meta:
        model = EmailSubscriber
        fields = ['subscriber_email',]

    def __init__(self, *args, **kwargs):
        super(EmailSubscriberForm, self).__init__(*args, **kwargs)
        self.fields['subscriber_email'].validators.append(aef.UniqueEmailSubscriberValidator)
        self.fields['subscriber_email'].validators.append(aef.EmailAddressValidator)

    def clean(self):
        super(EmailSubscriberForm, self).clean()
        return self.cleaned_data