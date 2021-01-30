from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def login(request):
    message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            message = "You are logged in..."
        else:
            message = "Invalide credentials"
    
    return render(request,'login.html',{'message': message})

def register(request):
    message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            user = User.objects.get(username = username)
            message = "Username exists! Try other username."
        except User.DoesNotExist:
            if password1 == password2:
                user = User.objects.create_user(
                username = username,
                password = password1
                )
                message = "Account Created Successfully!"
            else:
                message = "Passwords do not match!"
             
    return render(request, 'register.html', {'message' : message})