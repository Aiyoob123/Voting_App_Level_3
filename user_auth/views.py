# The following was imported
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserForm

# Create your views here.
# The below was given in the task 22 pdf
def user_login(request):
    return render(request, 'registration/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )

# The below was given in the task 22 pdf      
def show_user(request):
    print(request.user.username)
    return render(request, 'registration/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })

# New class called 'SignUpView'
class SignUpView(generic.CreateView):
    form_class = CustomUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    