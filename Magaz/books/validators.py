from django.core.exceptions import ValidationError

def BookTitleValidator(value):
    if any(char.isupper() for char in value):
        pass
    else:
        raise ValidationError('error - [title]')

def BookPriceValidator(value):
    if int(value) >= 15000:
        raise ValidationError('error - [price]')
    else:
        return value