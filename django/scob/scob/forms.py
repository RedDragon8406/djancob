from django import forms
from django.contrib.auth import get_user_model

class contact_form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری ..."}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "ایمیل (باید gmail باشد)"}))

    message = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "پیام شما ..."}))

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")

        return email



class Login_form(forms.Form):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری ..."}))
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"ایمیل ..."})
    )
    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور ..."}))

User = get_user_model()

class Register_form(forms.Form):
    error_css_class = 'text-danger'
    required_css_class = 'required'
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام کاربری ..."})
    )
    first_name = forms.CharField(
        label="نام",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام ..."})
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "نام خانوادگی ..."})
    )

    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "ایمیل ..."})
    )

    password = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور"})
    )

    password2 = forms.CharField(
        label="رمز عبور مجدد",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "رمز عبور مجدد"})
    )
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("username is taken")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Passwords must match")

        return data