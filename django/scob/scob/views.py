from django.contrib.auth import authenticate, login,logout, get_user_model
from django.shortcuts import render
from .forms import Login_form,Register_form,contact_form


def main_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    return render(request,"main.html",{})

def contact_page(request):
    form = contact_form(request.POST or None)
    context = {
        "form": form
    }
    return render(request,"contact.html",context)

def about_page(request):
    return render(request,"about.html",{})

def python_page(request):
    return render(request,"python.html",{})










def login_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    form = Login_form(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,email=email,password=password)
        if user is not None:
            login(request,user)
            context["form"] = Login_form()
            print("logined successfully")
        else:
            print("Error")

    return render(request,"login.html",context)


User = get_user_model()

def register_page(request):
    print(f"is user logged in : {request.user.is_authenticated}")
    form = Register_form(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username=username, email=email, password=password)
        login(request,new_user)
    return render(request,"register.html",context)

def logout_page(request):
    logout(request)
    return render(request,"logout.html")