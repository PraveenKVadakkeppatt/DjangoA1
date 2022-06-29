from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    employee_id=models.IntegerField()
    employee_name=models.CharField(max_length=255)
    employee_department=models.CharField(max_length=255)
    employee_age=models.IntegerField()
    employee_email=models.CharField(max_length=255)
    employee_contact=models.IntegerField()

