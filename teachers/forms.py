from django import forms

from .models import TeacherModel


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ["name", "surname", "birthday", "salary"]
        
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        fields = ["name", "surname", "birthday"]
        
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
