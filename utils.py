def is_valid_phone(phone):
    return phone.isdigit() and len(phone) in [10, 11]

def is_valid_email(email):
    return "@" in email and "." in email
