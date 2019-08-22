from django.db import models

# Create your models here.
class ServicesData(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100,unique=True)
    course_duration=models.CharField(max_length=100)
    course_state_date=models.DateField(max_length=100)
    course_start_time=models.TimeField(max_length=100)
    course_trainer_name=models.CharField(max_length=100)
    course_trainer_exp=models.CharField(max_length=100)
