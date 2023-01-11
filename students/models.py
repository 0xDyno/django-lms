import datetime

from django.db import models

# Create your models here.


class Student(models.Model):
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
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "students"