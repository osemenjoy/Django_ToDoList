from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import SignUpView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')), # not so sure yet
    path('signup/', SignUpView.as_view(), name= 'signup'),
    path('accounts/', include('accounts.urls')),
    path('task/', include('task.urls')),

]
