from django.db import models

from .validators import ValidateGroupStartDate

# Create your models here.


class GroupModel(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Group Name",
        db_column="name",
    )

    
    start_date = models.DateField(verbose_name="Start Date", validators=[ValidateGroupStartDate()])

    description = models.TextField(blank=True)
    
    class Meta:
        db_table = "groups"

    @classmethod
    def generate_fake_data(cls, number):
        if not isinstance(number, int) or number < 1:
            return

        from faker import Faker
    
        f = Faker()
        for _ in range(number):
            group = cls()
            group.name = " ".join(f.words(2)).capitalize()
            group.start_date = f.date()
            
            group.save()
