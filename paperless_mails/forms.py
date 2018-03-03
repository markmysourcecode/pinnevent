from django import forms
from django.core.exceptions import ValidationError
from paperless_mails.models import EmailSubscriber

def UniqueEmailSubscriberValidator(value):
    # set error message
    ErrMsg = {
        'email_subscription': 'oh, we\'ve just found out that you\'re already an active subscriber. Thanks for having interest on us.',
        }    

    if EmailSubscriber.objects.filter(email__iexact=value).exists():
        raise ValidationError(ErrMsg['email_subscription'])



class EmailSubscriberForm(forms.ModelForm):
    subscriber_email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                #'class': 'form-control form-control-sm',
                #'aria-describedby': 'password1Help',
                'placeholder': 'your email address',
            }),
        error_messages={
            'required': 'let\'s have your email address so we can reserve you the party!',
            'invalid': 'something is wrong, we can\'t find your email in the list of valid emails',
            #'invalid': 'You\'re awesome, but can you provide a valid email.',
            }
        )

    class Meta:
        model = EmailSubscriber
        fields = ['subscriber_email',]

    def __init__(self, *args, **kwargs):
        super(EmailSubscriberForm, self).__init__(*args, **kwargs)
        self.fields['subscriber_email'].validators.append(UniqueEmailSubscriberValidator)