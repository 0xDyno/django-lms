# Generated by Django 4.1.5 on 2023-01-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Name')),
                ('surname', models.CharField(db_column='surname', max_length=50, verbose_name='Surname')),
                ('birthday', models.DateField()),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]