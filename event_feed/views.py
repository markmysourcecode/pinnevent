from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from paperless_mails.forms import EmailSubscriberForm
from paperless_mails.models import EmailSubscriber
from application_events import application_functions as af
from paperless_mails import views as pme


import logging

def Index(request):

    if request.user.is_authenticated:
        return render(request, 'event_feed/index.html', { 'celebrate': True})

    else:
        # generate random background
        bg_load_image = af.RandomBackground()

        if request.method == 'POST':
            form = EmailSubscriberForm(request.POST)
            print(form.is_valid())

            if not form.is_valid():           
                return render(request, 'index.html', { 'form': form, 'bg_load_image': bg_load_image, })

            else:
                email = form.cleaned_data.get('subscriber_email')
                EmailSubscriber.objects.create(email=email)

                # return message base from success of sending email
                x = af.Send_Email_Subscription_With_SendGrid(email)
                if x == 202:
                    return redirect('application_events:thanksfor', thanks_for = 'subscribed')
                else:
                    return redirect('application_events:thanksfor', thanks_for = 'subscribed_failed')


        else:
            return render(request, 'index.html', {'form': EmailSubscriberForm(), 'bg_load_image': bg_load_image, })