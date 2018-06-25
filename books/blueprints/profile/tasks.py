from books.app import create_celery_app, mail

celery = create_celery_app()

@celery.task()
def send_email():

    # send single recipient; single email as sendgrid.mail.helpers.Email object
    mail.send_email(
        from_email='someone@yourdomain.com',
        to_email='pedx78@gmail.com',
        subject='Test Celery again',
        text='it works!!',
        # body='body ...'
    )

    return None



    # mail.send_email(
    #     from_email='admin@westcape.com',
    #     to_email=to,
    #     subject='Westcape Reset Password',
    #     text=reset_msg
    # )
