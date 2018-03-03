from django.shortcuts import render, redirect

from paperless_mails.forms import EmailSubscriberForm
from paperless_mails.models import EmailSubscriber
from application_events import application_functions as af

# sendgrid settings
import sendgrid
import os
from sendgrid.helpers.mail import *


def Index_With_Email_Subscription(request):

    # generate random background
    bg_load_image = af.RandomBackground()


    if request.method == 'POST':
        form = EmailSubscriberForm(request.POST)
        if not form.is_valid():
            #print("email in-valid")
            # messages.add_message(reksquest, messages.ERROR, 'There was some problems while creating your account. Please review some fields before submiting again.')
            return render(request, 'index.html', { 'form': form, 'bg_load_image': bg_load_image, })

        else:
            email = form.cleaned_data.get('subscriber_email')
            EmailSubscriber.objects.create(email=email)



            # send email via sendgrid
            SENDGRID_API_KEY_Z = os.environ.get('SENDGRID_API_KEY')
            print(SENDGRID_API_KEY_Z)
            sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY_Z)
            from_email = Email("pinneventofficial@gmail.com")
            subject = "Greetings from Pinnevent"
            to_email = Email(email)
            content = Content("text/plain", "Hello, Pinner! Thanks for having interest with what we are working. We'll connect to you soon.")
            mail = Mail(from_email, subject, to_email, content)
            response = sg.client.mail.send.post(request_body=mail.get())
            print(response.status_code)
            print(response.body)
            print(response.headers)

            # return message base from success of sending email
            if response.status_code == '202':
                return redirect('application_events:thanksfor', thanks_for = 'subscribed')
            else:
                return redirect('application_events:thanksfor', thanks_for = 'subscribed_failed')


    else:
        return render(request, 'index.html', {'form': EmailSubscriberForm(), 'bg_load_image': bg_load_image, })



