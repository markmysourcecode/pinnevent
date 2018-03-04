# what's this for?

import random


# sendgrid settings
import sendgrid
import os
from sendgrid.helpers.mail import *

import logging



def RandomBackground():
    # generate random backgrounds

    bg_image_name = "Bg-light-" + str(random.randint(0,3))
    return bg_image_name




def Send_Email_Subscription_With_SendGrid(to_email):
    # send subscription email using sendgrid

    logger = logging.getLogger(__name__)

    logger.info('trying to send an email')

    # set default apikey
    # ' apikey : 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
    SENDGRID_API_KEY_Z = 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
    try:
        SENDGRID_API_KEY_Z = os.environ.get('SENDGRID_API_KEY')
    except:
        pass


    #SENDGRID_API_KEY_Z = os.environ.get('SENDGRID_API_KEY')
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY_Z)
    from_email = Email("pinneventofficial@gmail.com")
    subject = "Greetings from Pinnevent"
    to_email = Email(email)
    content = Content("text/plain", "Hello, Pinner! Thanks for having interest with what we are working. We'll connect to you soon.")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    # test result
    logger.info(response.status_code)
    logger.info(response.body)
    logger.info(response.headers)


    return response.status_code