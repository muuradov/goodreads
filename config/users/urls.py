from django.urls import path

from .views import RegisterView, user_login, profile_view, Logout_view, UserLoginView

app_name = 'users'


urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('profile/', profile_view, name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', Logout_view.as_view(), name='logout'),
]