from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes #force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from .forms import RegistrationForm #UserEditForm
from .tokens import account_activation_token
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from .decorators import unauthenticated_user,allowed_users

@unauthenticated_user
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'login/profile.html',{'section': 'profile'})
# Create your views here.


def signup(request):
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate your Account'
    context={}
    return render(request,'registration/register.html',context)
'''message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
    else:
        registerForm = RegistrationForm()
    return render(request, 'registration/register.html', {'form': registerForm})'''

@unauthenticated_user
def loginppage(request):
    if request.user.is_authenticated:
        return render(request,'feed.html')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/feed')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})
'''@authenticated_user
def login_view(request):
    if request.user.is_authenticated:
        return render(request,'feed.html')
    
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/feed')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})'''


def feed_redirect(request):
    return redirect('/feed')





