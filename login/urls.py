'''from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

app_name = 'login'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', 
                                                authentication_form=UserLoginForm), name='login'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.accounts_register, name='register'),
    #path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
]'''

from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Django's built-in authentication views
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginppage, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=''), name='logout'),
    # Add more custom URLs as needed

]
