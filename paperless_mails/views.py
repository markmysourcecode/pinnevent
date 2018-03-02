from django.shortcuts import render, redirect

from paperless_mails.forms import EmailSubscriberForm
from paperless_mails.models import EmailSubscriber
from application_events import application_functions as af


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

            #print("email is valid")
            return redirect('application_events:thanksfor', thanks_for = 'subscribed')


    else:
        return render(request, 'index.html', {'form': EmailSubscriberForm(), 'bg_load_image': bg_load_image, })



