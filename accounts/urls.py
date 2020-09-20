from django.contrib import admin
from django.urls import path,include
from accounts import views
from django.contrib import admin
from django.views.generic.base import TemplateView





app_name = "accounts"



urlpatterns = [

    path('emp', views.emp),
    path('show',views.show),
    path('emp2', views.emp2),
    path('show2',views.show2),



    path('admin/', admin.site.urls),









]
