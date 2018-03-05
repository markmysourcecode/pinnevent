from django.shortcuts import render, redirect

from paperless_mails.forms import EmailSubscriberForm
from paperless_mails.models import EmailSubscriber
from application_events import application_functions as af

import logging



def Email_Subscription(request):

    # generate random background
    bg_load_image = af.RandomBackground()


    if request.method == 'POST':
        logger = logging.getLogger(__name__)


        form = EmailSubscriberForm(request.POST)
        if not form.is_valid():
            return render(request, 'index.html', { 'form': form, 'bg_load_image': bg_load_image, })

        else:
            # add subscriber
            email = form.cleaned_data.get('subscriber_email')
            EmailSubscriber.objects.create(email=email)

            # test
            logger.info(email)
            if email != "markusemailbox@gmail.com":
                EmailSubscriber.objects.create(email=email)


            # return message base from success of sending email
            x = af.Send_Email_Subscription_With_SendGrid(email)
            logger.info(x)
            if x == '202':
                return redirect('application_events:thanksfor', thanks_for = 'subscribed_failed')
            else:
                return redirect('application_events:thanksfor', thanks_for = 'subscribed_failed')


    else:
        return render(request, 'index.html', {'form': EmailSubscriberForm(), 'bg_load_image': bg_load_image, })
