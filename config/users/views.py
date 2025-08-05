from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import UserCreateForm


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



@login_required(login_url='users:login')
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})


class Logout_view(View):
    def get(self, request):
        logout(request)

        return redirect("home")