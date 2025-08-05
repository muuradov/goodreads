from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreateForm, LoginForm


class RegisterView(View):
    def get(self, request):
        create_user = UserCreateForm()

        context = {
            'form':create_user
        }
        return render(request=request, template_name='register.html', context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request=request, template_name='register.html', context=context)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username yoki parol xato!')

    return render(request, 'login.html')

class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, 'You are now logged in')

            return redirect('home')
        else:
            return render(request=request, template_name='login.html', context={'form': login_form})


@login_required(login_url='users:login')
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


class Logout_view(View):
    def get(self, request):
        logout(request)

        return redirect("home")