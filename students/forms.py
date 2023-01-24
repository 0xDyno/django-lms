from django.core.validators import ValidationError
from django.forms import ModelForm

from . import utils
from .models import StudentModel


UA_SIM_PROVIDERS = {"039", "067", "068", "096", "097", "098", "050", "066", "095",
                    "099", "063", "073", "093", "091", "092", "089", "094"}
UA_PHONE_NUMBER_LENGTH = 12


class StudentForm(ModelForm):
    class Meta:
        model = StudentModel
        fields = ["name", "surname", "birthday", "city", "email", "phone_number"]
        
    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        
        only_numbers = utils.get_only_numbers(phone)
        
        # this will work only for UA phone numbers
        # to support all phone numbers - it's required to divide country code & number
        
        if len(only_numbers) != UA_PHONE_NUMBER_LENGTH:
            message = f"Wrong phone number, should be {UA_PHONE_NUMBER_LENGTH} numbers, got {len(only_numbers)}"
            raise ValidationError(message=message)
        elif only_numbers[:3] != "380":
            raise ValidationError(message="That's not UA number")
        elif only_numbers[2:5] not in UA_SIM_PROVIDERS:
            raise ValidationError(message="There are no such sim-card provides")
        else:
            country_code = only_numbers[:3]
            provider = only_numbers[3:5]
            numbers = "{}-{}-{}".format(only_numbers[5:8], only_numbers[8:10], only_numbers[10:])
    
            phone_format = f"{country_code} {provider} {numbers}"
            return phone_format
