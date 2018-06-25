from flask import flash, current_app
from itsdangerous import URLSafeTimedSerializer

from books.app import db
from books.blueprints.auth.models import User
from . import auth


@auth.route('/confirm/<token>')
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        email = confirm_serializer.loads(token, salt='email-confirmation-salt', max_age=86400)
    except:
        flash('The confirmation link is invalid or has expired.', 'error')
        return "Please try again"
 
    user = User.query.filter_by(email=email).first()
 
    if user.email_confirmed:
        flash('Account already confirmed. Please login.', 'info')
    else:
        user.email_confirmed = True
        # user.email_confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
        flash('Thank you for confirming your email address!')
        print('success - email')
 
    return "Thank you"
