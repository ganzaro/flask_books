import datetime
import pytz

def update_activity_tracking(user, ip_address):
    """
    Update various fields on the user that's related to meta data on their
    account, such as the sign in count and ip address, etc..

    :param ip_address: IP address
    :type ip_address: str
    :return: SQLAlchemy commit results
    """
    user.sign_in_count += 1

    user.last_sign_in_on = user.current_sign_in_on
    user.last_sign_in_ip = user.current_sign_in_ip

    user.current_sign_in_on = datetime.datetime.now(pytz.utc)
    user.current_sign_in_ip = ip_address

    return save()