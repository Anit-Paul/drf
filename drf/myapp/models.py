from django.db import models
from django.utils import timezone
# Create your models here.
class Student(models.Model):
    MY_SCHOOL=[
        ('AB','AB School'),
        ('BB','BB School'),
        ('CB','CB School'),
    ]
    name=models.CharField(max_length=100)
    date=models.DateTimeField(default=timezone.now)
    school=models.CharField(max_length=2,choices=MY_SCHOOL)
    
    def __str__(self):
        return self.name