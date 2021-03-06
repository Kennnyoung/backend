import re
from jsonschema import draft4_format_checker
from validate_email import validate_email

PASSWORD_RE = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
USERNAME_RE = re.compile("^([a-zA-Z0-9-]){3,12}$")
EMAIL_MIN = 5
EMAIL_MAX = 40

def check_given_string(func):
    def wrapper(stringVal):
        if not isinstance(stringVal, str):
            return False
        return func(stringVal)

    return wrapper


@check_given_string
@draft4_format_checker.checks('secure_password')
def is_valid_password(val):
    return PASSWORD_RE.match(val)


@check_given_string
@draft4_format_checker.checks('email')
def is_valid_email(email):
    if len(email) < EMAIL_MIN or len(email) > EMAIL_MAX:
        return False
    return validate_email(email)


@check_given_string
@draft4_format_checker.checks('username')
def is_valid_username(username):
    return USERNAME_RE.match(username) is not None

