from django.shortcuts import render, redirect
from accounts.forms import AccountForm,ResultForm
from accounts.models import Account,Result
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from . import forms,models
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    accounts = User.objects.count()
    return render(request, 'home.html', {
        'accounts': accounts
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


@login_required
def secret_page(request):
    return render(request, 'secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'








# Create your views here.
@login_required
def emp(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = AccountForm()
    return render(request,'index.html',{'form':form})
def show(request):
    accounts = Account.objects.all()
    return render(request,"show.html",{'accounts':accounts})


def emp2(request):
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show2')
            except:
                pass
    else:
        form = ResultForm()
    return render(request,'add-result.html',{'form':form})
def show2(request):
    accounts = Result.objects.all()
    return render(request,"showresult.html",{'accounts':accounts})
def edit(request, id):
    accounts = Account.objects.get(id=id)
    return render(request,'edit.html', {'accounts':accounts})
def update(request, id):
    accounts = Account.objects.get(id=id)
    form = AccountForm(request.POST, instance = accounts)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'accounts': accounts})
def destroy(request, id):
    accounts = Account.objects.get(id=id)
    accounts.delete()
    return redirect("/show")
