from django.core.exceptions import ValidationError


def validate_unique_email(value):
    from .models import StudentModel
    
    all_emails = StudentModel.objects.values_list("email", flat=True)
    if value in all_emails:
        raise ValidationError(message=f"Email {value} already exist in the system")
