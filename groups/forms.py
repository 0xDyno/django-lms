from django import forms

from .models import GroupModel


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = GroupModel
        fields = ["name", "start_date", "description"]
    
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"style": "text-align: center;",
                                                 "placeholder": "Write group's description"})
        }
        


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = GroupModel
        fields = ["description"]
        
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"style": "text-align: center;",
                                                 "placeholder": "Write group's description"})
        }
    
