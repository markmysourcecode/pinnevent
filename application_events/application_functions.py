# what's this for?

import random


# sendgrid settings
import sendgrid
import os
from sendgrid.helpers.mail import *
import json

import logging


# applications models
from paperless_mails.models import EmailSubscriber
from accounts.models import User


# validators
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator



# name me later
# -----------------------------------------------------------------------------------------------------------------------------------------------

def RandomBackground():
    # generate random backgrounds

    bg_image_name = "Bg-light-" + str(random.randint(0,3))
    return bg_image_name


def GetSendGridAPIKeyInLocalSettings():
    # read localsettings if it exist
    try:
        from random_events import local_settings
        return getattr(local_settings, "SENDGRID_API_KEY_LOCAL")
    except ImportError:
        return None
    






# emails
# -----------------------------------------------------------------------------------------------------------------------------------------------

def Send_Email_Subscription_With_SendGrid(to_email):
    # send subscription email using sendgrid

    try:
        SENDGRID_API_KEY_Z = os.environ.get('SENDGRID_API_KEY')
    except:
        pass


    if SENDGRID_API_KEY_Z is None:
        SENDGRID_API_KEY_Z = GetSendGridAPIKeyInLocalSettings()

    '''sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY_Z)
    from_email = Email("pinneventofficial@gmail.com")
    subject = "Greetings from Pinnevent"
    to_email = Email(to_email)
    content = Content("text/plain", "Hello, Pinner! Thanks for having interest with what we\'re working. We'll connect to you soon.")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())'''

    #return response.status_code
    return 202





# validators
# -----------------------------------------------------------------------------------------------------------------------------------------------

def UniqueEmailSubscriberValidator(value):
    # set error message
    error_messages = { 'email_subscription': 'oh, we\'ve just found out that you\'re already an active subscriber. Thanks for having interest on us.', }    

    if EmailSubscriber.objects.filter(email__iexact=value).exists():
        raise ValidationError(error_messages['email_subscription'])



def UniqueEmailSignupValidator(value):
    error_messages = {'email_signup': 'something is wrong, the email address you\'ve just provided are already a registered account.', }    

    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError(error_messages['email_signup'])



def EmailAddressValidator(value):
    # set error message
    error_messages={ 'invalid': 'We appreciate it, but we need you to provide a valid email address.', }

    validator = EmailValidator()
    try:
        validator(value)
    except ValidationError:
        raise ValidationError(error_messages['invalid'])

