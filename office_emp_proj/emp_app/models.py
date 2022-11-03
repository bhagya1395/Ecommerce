from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# superusers = User.objects.filter(is_superuser=True)


class Department(models.Model):
    name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=150)
    dept = models.ForeignKey(Department, on_delete=models.Model)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)
