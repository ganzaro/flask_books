from flask import render_template, url_for, current_app
from itsdangerous import URLSafeTimedSerializer

from books.app import create_celery_app, mail
from books.blueprints.auth.models import User

celery = create_celery_app()

@celery.task()
def send_confirmation_email(user_email):
    print('send_confirmation_email called')
    confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
 
    confirm_url = url_for(
        'auth.confirm_email',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)
 
    html = render_template(
        'auth/mail/email_confirmation.html',
        confirm_url=confirm_url)
 
    # send_email('Confirm Your Email Address', [user_email], html)
    mail.send_email(
        from_email='adminx@wc.com',
        # to_email='ganzaro.af@gmail.com',
        to_email=user_email,
        subject='Confirm Email Address', 
        text=html
    )
    print('after mail sent')

