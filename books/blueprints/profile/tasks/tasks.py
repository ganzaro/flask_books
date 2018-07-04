from books.app import create_celery_app, mail

celery = create_celery_app()

@celery.task()
def send_email():

    # send single recipient; single email as sendgrid.mail.helpers.Email object
    mail.send_email(
        from_email='someone@yourdomain.com',
        to_email='ganzaro.af@gmail.com',
        subject='Test Celery mail',
        text='it works!!',
        personalizations=''
        # body='body ...'
    )

    return None


