def email_masking(email, masking_dict={'@': ' [ at ] ', '.': ' [ dot ] '}):
    """Parse the email address where the dots(.) and the at(@) will be repalced
     by a string.
    >>> str(email_masking(email="chris.tucker@gmail.com"))
    'chris [ dot ] tucker [ at ] gmail [ dot ] com'
    >>> custom_masking_dict = {'.': '({dot})', '@': '[at]'}
    >>> str(email_masking(email="chris.tucker@gmail.com", masking_dict=custom_masking_dict))
    'chris({dot})tucker[at]gmail({dot})com'
    """
    replaced_dots = masking_dict['.'].join(email.split('.'))
    return masking_dict['@'].join(replaced_dots.split('@'))

def email_recovery(masked_email, masking_dict={'@': ' [ at ] ', '.': ' [ dot ] '}):
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
