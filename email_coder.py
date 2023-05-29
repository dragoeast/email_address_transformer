def email_masking(email):
    """Parse the email address where the dots(.) and the at(@) will be repalced
     by a string.
    >>> str(email_masking(email="chris.tucker@gmail.com"))
    'chris [ dot ] tucker [ at ] gmail [ dot ] com'
    """
    replaced_dots = ' [ dot ] '.join(email.split('.'))
    return ' [ at ] '.join(replaced_dots.split('@'))
