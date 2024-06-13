
# Create your views here.
#Below are all my imports
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Choice
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Below are few new functions
# 'def' was used
def home(request):
    """
    View function for the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with rendered home template.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'voting_app/home.html', context)

@login_required
def detail(request, question_id):
    """
    View function for the detail page of a specific question.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question.

    Returns:
        HttpResponse: The HTTP response object with rendered detail template.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'voting_app/detail.html', {'question': question})

@login_required
def vote(request, question_id):
    """
    View function to handle voting on a specific question.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question.

    Returns:
        HttpResponse: The HTTP response object with rendered template if there's an error,
                      or a redirect to the results page on successful vote.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'voting_app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('results', question_id=question.id)

@login_required
def results(request, question_id):
    """
    View function to display the results of a specific question.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the question.

    Returns:
        HttpResponse: The HTTP response object with rendered results template.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'voting_app/results.html', {'question': question})

def register(request):
    """
    View function to handle user registration.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with rendered registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    """
    View function to handle user login.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with rendered login form.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    """
    View function to handle user logout.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with a redirect to the home page.
    """
    logout(request)
    return redirect('home')
