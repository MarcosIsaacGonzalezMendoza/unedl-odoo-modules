# -*- coding: utf-8 -*-

import re

EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    if re.match(EMAIL_REGEX,email):
        return True
    else:
        return False

def is_valid_name(name):
    if name.isalpha() or name.replace(" ", "").isalpha():
        return True
    else:
        return False

def is_valid_phone(phone):
    if len(phone) == 10:
        if phone.isdigit():
            return True
        else:
            return False
    else:
        return False