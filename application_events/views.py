# this view will handle non speicific functionalities of the app

from django.shortcuts import render



def TermsOfServicesView(request):
    return render(request, 'application_events/tos.html',)


# give thanks to the action
def ThankYouView(request, **kwargs):

    # msg list
    thank_you_for_dict = {
            'registered': 'some message here for complete registration.',
            'subscribed': 'some message here for complete subscription.',
            'welcome-first': 'some message here for authenticated login.',
            'not_sure': 'Ooops, there\'s something wrong with this page. Don\'t worry it is not you, it is us.',
        }

    # validate thank you for message
    try:
        thank_you_for = thank_you_for_dict[kwargs['thanks_for']]
    except KeyError:
        thank_you_for = thank_you_for_dict['not_sure']

    print(thank_you_for)
    
    return render(request, 'application_events/thanks.html', {'thank_you_for': thank_you_for })


