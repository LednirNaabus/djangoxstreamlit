from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    employed_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.position}"