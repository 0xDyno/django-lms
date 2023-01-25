from django import forms

from . import utils
from .models import StudentModel


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ["name", "surname", "birthday", "city", "email", "phone_number"]
        
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number").strip()
        return utils.normalize_phone_number(phone_number)
    

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ["name", "surname", "birthday", "city", "phone_number"]
        
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number").strip()
        return utils.normalize_phone_number(phone_number)
