from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth








urlpatterns = [

    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('member.urls')),


]
