
# These are my imports
from django.urls import path
from . import views

# Below are my url for the pages
urlpatterns = [
    path('', views.home, name='home'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/vote/', views.vote, name='vote'),
    path('question/<int:question_id>/results/', views.results, name='results'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
