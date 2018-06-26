from flask import flash, current_app, request, render_template
from itsdangerous import URLSafeTimedSerializer

from books.app import db
from books.blueprints.auth.models import User
from . import auth
from . forms import PasswordResetForm


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



@auth.route('/account/password_reset', methods=['GET', 'POST'])
def password_reset():
    form = PasswordResetForm(reset_token=request.args.get('reset_token'))

    if form.validate_on_submit():
        u = User.deserialize_token(request.form.get('reset_token'))

        if u is None:
            flash('Your reset token has expired or was tampered with.',
                  'error')
            # return redirect(url_for('auth.begin_password_reset'))
            return 'Please reset passwprd again'

        form.populate_obj(u)
        u.password = User.encrypt_password(request.form.get('password'))
        u.save()

        # if login_user(u):
        #     flash('Your password has been reset.', 'success')
        #     return redirect(url_for('user.settings'))

    return render_template('auth/password_reset.html', form=form)


