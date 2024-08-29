from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100,null=True)
    fee = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100,null=True)
    address = models.TextField(null=True)
    age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.name