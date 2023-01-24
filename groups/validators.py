import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateGroupStartDate:
    
    def __init__(self, date: datetime.date = None):
        if date and isinstance(date, datetime.date):
            self.date = date
        else:
            self.date = datetime.date.today()
    
    def __call__(self, *args, **kwargs):
        group_date = args[0]
        if group_date < self.date:
            message = "Group can't start in the past. Current date {}, you gave {}".format(self.date, group_date)
            raise ValidationError(message=message)
