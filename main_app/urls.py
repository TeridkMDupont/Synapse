from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup')
]