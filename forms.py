from django import forms
from django.contrib.auth.models import User
from registration.models import Register


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("passwords must match!")
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not'@gmail.com' in email:
            raise forms.ValidationError('only gmail accounts required!')

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('this email has taken!')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_qs = User.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError('this username has taken!')
        return username


class RegisterModelForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            'first_name',
            'last_name'
        ]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     username_qs = User.objects.filter(username=username)
    #     if username_qs.exists():
    #         raise forms.ValidationError('this username has taken!')
    #     return username

    # def clean(self):
    #     data = self.cleaned_data
    #     password = self.cleaned_data.get('password')
    #     password2 = self.cleaned_data.get('password2')
    #     if password2 != password:
    #         raise forms.ValidationError("passwords must match!")
    #     return data