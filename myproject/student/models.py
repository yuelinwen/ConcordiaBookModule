from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username