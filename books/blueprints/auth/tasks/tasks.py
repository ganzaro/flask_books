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
 
    # send_email('Confirm Email Address', [user_email], html)
    mail.send_email(
        from_email='info@wc.com',
        to_email=user_email,
        subject='Confirm Email Address', 
        text=html
    )
    print('after mail sent')
    return None


@celery.task()
def deliver_password_reset_email(user_email):
    print('####################################')
    print('deliver password_reset_email called')    
    confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
 
    confirm_url = url_for(
        'auth.password_reset',
        token=confirm_serializer.dumps(user_email, salt='email-confirmation-salt'),
        _external=True)
 
    html = render_template(
        'auth/mail/password_reset.html',
        confirm_url=confirm_url)
 
    # send_email('Confirm Email Address', [user_email], html)
    mail.send_email(
        from_email='info@wc.com',
        to_email=user_email,
        subject='Reset Password', 
        text=html
    )
    print('after reset mail sent')
    print('************************************')
    return None


# @celery.task()
# def deliver_password_reset_email(user_email, reset_token):

#     usr = User.query.get(user_email)
#     print('deliver password_reset_email called')
#     # usr = User.query.filter_by(email=user_email).first_or_404()

#     to = usr.email
#     link = url_for('auth.password_reset', reset_token=reset_token)
#     reset_msg = 'your password reset email link {0}'.format(link)


#     print('linkz {}'.format(reset_msg))
#     print('####################################')

#     mail.send_email(
#         from_email='la@wc.com',
#         to_email=user_email,
#         subject='Reset Password',
#         text=reset_msg
#     )

#     print('deliver task sent')
#     return None




