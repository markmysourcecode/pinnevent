# this view will handle non speicific functionalities of the app

from django.shortcuts import render



def TermsOfServicesView(request):
    return render(request, 'application_events/tos.html',)


# give thanks to the action
def ThankYouView(request, **kwargs):

    # msg list
    thank_you_for_dict = {
            'registered': 'some message here for complete registration.',
            'subscribed': 'Thanks for subscribing! You\'ll be receiving our invitation soon. We are excited to meet you in the party!',
            'welcome-first': 'some message here for authenticated login.',
            'pinningwithus': 'some message here after using pinnevent.',

            'subscribed_failed': 'Ooops, there\'s something wrong with how the mail was sent. Don\'t worry it is not you, it is us.',
            'not_sure': 'Ooops, there\'s something wrong with this page. Don\'t worry it is not you, it is us.',
        }

    celebrate = False

    # validate thank you for message
    try:
        thank_you_for = thank_you_for_dict[kwargs['thanks_for']]
        celebrate = True
    except KeyError:
        thank_you_for = thank_you_for_dict['not_sure']

    print(thank_you_for)
    
    return render(request, 'application_events/thanks.html', {'thank_you_for': thank_you_for, 'celebrate': celebrate })


