# These are my imports
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Below is a new class called 'CustomUserForm'
# This is for my signup page
class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'password1', 'password2' ]
        