from django.db import models
from django.db.models import IntegerField, Model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    typ=models.CharField(max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Test(models.Model):
    title_name=models.CharField(max_length=200)
    date=models.DateField(blank=True, null=True)
    percentage_score=models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    course=models.ForeignKey(Course, on_delete=models.CASCADE)