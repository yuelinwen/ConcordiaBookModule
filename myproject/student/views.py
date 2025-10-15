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
            # 根据 username 查找学生
            student = Student.objects.get(username=username)
            # 检查密码是否匹配
            if check_password(password, student.password):
                # 登录成功，这里可以存 session
                request.session['student_id'] = student.id
                request.session['username'] = student.username
                messages.success(request, f"Welcome {student.username}!")
                # 处理 next 参数（优先返回到 next，如果没有则去 home）
                next_url = request.GET.get('next') or request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('/')   # 或 return redirect('/')
            else:
                messages.error(request, "Invalid username or password")
        except Student.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        # 检查 student_id 是否已经存在
        if Student.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student ID already exists")
            return render(request, 'register.html')

        # 密码可以用哈希保存，提高安全性
        hashed_password = make_password(password)

        # 创建新的学生记录
        student = Student(username=username, student_id=student_id, password=hashed_password)
        student.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')  # 创建成功跳转到登录页面
    return render(request, 'register.html')
