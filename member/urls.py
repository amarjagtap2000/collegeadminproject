from django.contrib import admin
from django.urls import path, include
from member import views
from django.contrib import admin
from django.views.generic.base import TemplateView

app_name = "member"

urlpatterns = [

    path('emp1', views.emp1),
    path('show1', views.show1),

    path('admin/', admin.site.urls),

]
