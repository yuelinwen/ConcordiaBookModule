from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            student = Student.objects.get(username=username)
            if check_password(password, student.password):
                request.session['student_id'] = student.id
                request.session['username'] = student.username
                messages.success(request, f"Welcome {student.username}!")
                next_url = request.GET.get('next') or request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        except Student.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not student_id or not password:
            messages.error(request, "All fields are required!")
            return render(request, 'register.html')

        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists")
            return render(request, 'register.html')

        hashed_password = make_password(password)

        student = Student(username=username, student_id=student_id, password=hashed_password)
        student.save()

        messages.success(request, "Account created successfully!")
        return redirect('login') 

    return render(request, 'register.html')

