from django.db import models


class TeacherModel(models.Model):
    
    name = models.CharField(max_length=50, verbose_name="Name", db_column="name")
    surname = models.CharField(max_length=50, verbose_name="Surname", db_column="surname")
    birthday = models.DateField()
    salary = models.IntegerField()
    # yearly or monthly.. interesting question
    
    class Meta:
        db_table = "teachers"

    def __str__(self):
        return "Teacher {} {} ({})".format(self.name, self.surname, self.id)

    @classmethod
    def generate_fake_data(cls, number):
        if not isinstance(number, int) or number < 1:
            return
    
        from faker import Faker
        from random import randint
    
        f = Faker()
        for _ in range(number):
            teacher = cls()
            teacher.name = f.first_name()
            teacher.surname = f.last_name()
            teacher.birthday = f.date()
            teacher.salary = randint(1000000, 9999999)
            
            teacher.save()
