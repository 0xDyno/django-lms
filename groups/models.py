from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Group Name",
        db_column="name",
    )

    # without additional information about the realisation and usage it's impossible
    # to create necessary fields, because they vary depend on the usage
    
    start_date = models.DateField(
        verbose_name="Start Date",
    )

    description = models.TextField()
    
    class Meta:
        db_table = "groups"