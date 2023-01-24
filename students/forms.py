from django.forms import ModelForm

from .models import StudentModel


class StudentForm(ModelForm):

    class Meta:
        model = StudentModel
        fields = ["name", "surname", "birthday", "city", "email"]
