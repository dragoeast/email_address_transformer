Email = str
Masked_Email = str
Dot = str
At = str
Masked_Dot = str
Masked_At = str
Masking_Dictionary = dict[Dot|At, Masked_Dot|Masked_At]

def email_masking(email: Email, masking_dict: Masking_Dictionary={'@': ' [ at ] ', '.': ' [ dot ] '}):
    """Parse the email address where the dots(.) and the at(@) will be repalced
     by a string.
    >>> str(email_masking(email="chris.tucker@gmail.com"))
    'chris [ dot ] tucker [ at ] gmail [ dot ] com'
    >>> custom_masking_dict = {'.': '({dot})', '@': '[at]'}
    >>> str(email_masking(email="chris.tucker@gmail.com", masking_dict=custom_masking_dict))
    'chris({dot})tucker[at]gmail({dot})com'
    """
    partialy_masked = masking_dict['.'].join(email.split('.'))
    return masking_dict['@'].join(partialy_masked.split('@'))

def email_recovery(masked_email: Masked_Email, \
                   masking_dict: Masking_Dictionary={'@': ' [ at ] ', '.': ' [ dot ] '}):
    """Return the email from the masked form to the original form.
    >>> email_recovery(masked_email='chris [ dot ] tucker [ at ] gmail [ dot ] com')
    'chris.tucker@gmail.com'
    >>> custom_masking_dict = {'.': '({dot})', '@': '[at]'}
    >>> email_recovery(masked_email='chris({dot})tucker[at]gmail({dot})com',\
        masking_dict=custom_masking_dict)
    'chris.tucker@gmail.com'
    """
    partially_recovered_email = '@'.join(masked_email.split(masking_dict['@']))
    return '.'.join(partially_recovered_email.split(masking_dict['.']))
