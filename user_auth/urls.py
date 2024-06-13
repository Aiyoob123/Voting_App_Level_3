# Below I imported path from 'django.urls'
from django.urls import path
# Below I imported views from '. import'
from . import views
# SignUpView was imported from .views
from .views import SignUpView

# Below i added app_name as 'polls' to set the application namespace
app_name = 'user_auth'
# Below are the urls
urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
        name='authenticate_user'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('show_user', views.show_user, name="show_user")
]
