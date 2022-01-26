from users.decorators import unauthenticated_user
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.forms.widgets import EmailInput
from django.shortcuts import redirect, render
from .import form
from users.form import AddressForm, CreateUserForm, LoginForm, User_Update_Form
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


# Register members
@unauthenticated_user
def Register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, "Account created successful "+username)
            return redirect('login')
    context = {'form': form}
    return render(request, "users/regist.html", context)


# Allow people to signIn
@unauthenticated_user
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, ' Username or Password is incorrect')
    context = {}
    return render(request, "users/login.html", context)


# Allow the customer to provide ur address
def address(request):
    form = AddressForm()
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            f_name = form.cleaned_data.get('f_name')
            l_name = form.cleaned_data.get('l_name')
            name = f_name+''+l_name
            messages.success(request, "Address updated successful "+name)
            return redirect('profile')
    context = {'form': form}
    return render(request, 'users/address.html', context)


def Logout(request):
    return render(request, 'users/logout.html')


# Updating the profile of the user
@login_required
def profile(request):
    if request.method == 'POST':

        u_form = User_Update_Form(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()

            messages.success(request, f'Account Updated sucessfuly!')
            return redirect('profile')
    else:
        u_form = User_Update_Form(instance=request.user)

    context = {
        'u_form': u_form,

    }
    return render(request, 'users/profile.html', context)


# Implement how we can delete customers accounts
'''def deleteuser(request):
    current_user = request.user
    if request.method == 'POST':
        current_user.delete()
        redirect('home')
    context = {'current_user': current_user}
    return render(request, 'user/profile.html', context)'''
