from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Courses(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Details(models.Model):
    name = models.CharField(max_length=20)
    date_of_brith = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField
    email = models.EmailField()
    address = models.CharField(max_length=300)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    courses = models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True)
    purpose = models.CharField(max_length=20)
    materials_provide = models.CharField(max_length=10)

    def __str__(self):
        return self.name
