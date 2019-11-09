from django.urls import path, include
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('signup',views.SignUp.as_view(),name='signup'),
    path('login/',views.logIn,name='login'),
    path('logout/',views.logOut,name='logout'),
]