# Generated by Django 4.1.5 on 2023-01-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='First Name')),
                ('surname', models.CharField(db_column='surname', max_length=50, verbose_name='Surname')),
                ('birthday', models.DateField()),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]
