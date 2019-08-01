from django.shortcuts import render
from django.template import RequestContext
from . form import LoginForm, course_registration_form, test_scores_registration_form
from django.contrib.auth.models import User
from . models import Course, Test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "home/home.html")
# Create your views here.

def Create_New(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            messages.success(request, 'Account has been created. Go to Login page.')
    else:
        form=UserCreationForm()
    return render(request, 'home/register.html',{'form': form})

def User_Login(request):
    if request.method == "POST":
        username=request.POST['user_name']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/dashboard')
        else:
            messages.error(request, 'username or password is incorrect')
            return redirect('/home/login')
    else:
        form=LoginForm()
        return render(request, 'home/signin.html', {'form': form})

def user_dashboard(request):
    if request.user.is_authenticated :
        course_items=Course.objects.filter(user=request.user)
        return render(request, 'home/dashboard.html', {'course_items': course_items})
    else:
        return redirect('/home/login')

def user_logout(request):
    logout(request)
    return redirect('/home')

def create_course(request):
    if request.user.is_authenticated :
        if request.method == "POST":
            form = course_registration_form(request.POST)
            if form.is_valid():
                new_course = form.save(commit=False)
                new_course.course_name=form.cleaned_data['course_name']
                new_course.typ=form.cleaned_data['typ']
                new_course.user=request.user
                new_course.save()
                return redirect('/home/dashboard')

        else:
            form = course_registration_form()
        return render(request, 'home/createcourse.html', {'form': form})
    else:
        return redirect('/home/login')
def course_board(request, id):
    if request.user.is_authenticated:
        Citem = Course.objects.get(pk=id)
        if request.method == "POST":
            form = test_scores_registration_form(request.POST)
            if form.is_valid():
                new_test_score= form.save(commit=False)
                new_test_score.title_name = form.cleaned_data['title_name']
                new_test_score.percentage_score = form.cleaned_data['percentage_score']
                new_test_score.course = Citem
                new_test_score.save()
                messages.success(request, 'created.')
        form=test_scores_registration_form()
        test_scores = Test.objects.filter(course=Citem)
        return render(request, 'home/marks.html', {'test_scores': test_scores, 'form': form, 'course_id': id})
    else:
        return redirect('/home/login')

def delete_test(request, course_id, test_id):
        test=Test.objects.get(pk=test_id)
        test.delete()
        return redirect('/home/'+str(course_id))