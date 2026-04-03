from django.shortcuts import render, redirect

def user_login(request):
    return render(request, 'chat/login.html')

def user_logout(request):
    # Optional logout logic
    return redirect('login')

def chat_home(request):
    return render(request, 'chat/chat_home.html')