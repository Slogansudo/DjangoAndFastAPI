from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Address, TravelCategory, Travels, Comments

# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login_users.html')

    def post(self, request):
        user = {
            "username": request.POST.get("username"),
            "password": request.POST.get("password")
        }
        login_form = AuthenticationForm(data=user)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return HttpResponse("Logged in successfully")

class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register_user.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if len(password1) < 4:
            return render(request, 'auth/register_user.html', {'comment': 'at least 4 characters'})
        if password1 != password2:
            return render(request, 'auth/register_user.html', {'comment': 'The password was entered incorrectly'})
        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(username) == 0:
            return render(request, 'auth/register_user.html', {'comment': 'fields must be filled'})
        users = User.objects.filter(username=username)
        if not users:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('landing')
        else:
            return render(request, 'auth/register_user.html', {'comment': 'The following user exists'})


class AddressView(LoginRequiredMixin, View):
    def get(self, request):
        address = Address.objects.all()
        return render(request, 'places.html', {'addresses': address})

