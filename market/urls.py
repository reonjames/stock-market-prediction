from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name='home_url'),
    path('signup/', views.signup, name='signup_url'),
    path('login/',views.login,name='login_url'),
    path('forget/',views.forget,name='forget_url'),
]