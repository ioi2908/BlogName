from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model, logout, login, authenticate
from forms import RegisterForm,RegisterModelForm, LoginForm

User = get_user_model()


def register_page(request):
    if request.method == 'POST':
        form_normal = RegisterForm(request.POST or None)
        form_model = RegisterModelForm(request.POST or None)

        if form_model.is_valid() and form_normal.is_valid():
            username = form_normal.cleaned_data.get('username')
            email = form_normal.cleaned_data.get('email')
            password = form_normal.cleaned_data.get('password')
            new_user = User.objects.create_user(username=username,
                                                email=email, password=password)

            # form_model.save()
            return redirect('login')

    form_normal = RegisterForm()
    form_model = RegisterModelForm()

    arg = {
        'form_normal': form_normal,
        'form_model': form_model
    }

    return render(request, template_name='register.html',context=arg)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    form = LoginForm()
    args = {'form':form}
    return render(request, template_name='login.html', context=args)


@login_required()
def logout_page(request):
    logout(request)
    return render(request, template_name='logout.html')


@login_required()
def profile_page(request):
    return render(request, template_name='profile.html')


def home(request):
    return render(request, template_name='home.html')



@login_required()
def about_page(request):
    return render(request, template_name='about.html')

