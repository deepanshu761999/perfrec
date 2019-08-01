from django import forms
from django.forms import ModelForm
from . models import Course, Test
from django.core.validators import MaxValueValidator, MinValueValidator
class LoginForm(forms.Form):
    user_name=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)

class course_registration_form(ModelForm):
    course_name=forms.CharField(max_length=100, required=True)
    class Meta:
        model = Course
        fields = ['course_name','typ']

class test_scores_registration_form(ModelForm):
    title_name=forms.CharField(max_length=100, required=True)
    percentage_score = forms.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    class Meta:
        model = Test
        fields =['title_name', 'percentage_score']