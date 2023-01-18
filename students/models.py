import datetime

from django.db import models

from .validators import validate_unique_email

# Create your models here.

DOMAINS = ["gmail.com", "yahoo.com", "icloud.com", "proton.me"]


class StudentModel(models.Model):
    # For CharField blank & null are False by default
    name = models.CharField(
        max_length=50,
        verbose_name="First Name",
        db_column="name",
    )
    surname = models.CharField(
        max_length=50,
        verbose_name="Surname",
        db_column="surname",
    )
    birthday = models.DateField()
    city = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    email = models.EmailField(validators=[validate_unique_email])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{} {} ({})".format(self.name, self.surname, self.id)
    
    class Meta:
        db_table = "students"
    
    @classmethod
    def generate_fake_data(cls, number):
        if not isinstance(number, int) or number < 1:
            return
        
        from faker import Faker
        
        f = Faker()
        for _ in range(number):
            student = cls()
            student.name = f.first_name()
            student.surname = f.last_name()
            student.birthday = f.date()
            student.city = f.city()
            
            domain = f.random.choice(DOMAINS)
            student.email = f.email(domain=domain)
            
            student.save()
