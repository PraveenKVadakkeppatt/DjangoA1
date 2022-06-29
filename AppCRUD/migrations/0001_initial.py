# Generated by Django 4.0.4 on 2022-06-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('employee_name', models.CharField(max_length=255)),
                ('employee_department', models.CharField(max_length=255)),
                ('employee_age', models.IntegerField()),
                ('employee_email', models.CharField(max_length=255)),
                ('employee_contact', models.IntegerField()),
            ],
        ),
    ]