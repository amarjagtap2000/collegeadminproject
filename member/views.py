from django.shortcuts import render, redirect
from member.forms import StaffForm
from member.models import Staff
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from . import forms,models
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse






# Create your views here.
def emp1(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show1')
            except:
                pass
    else:
        form = StaffForm()
    return render(request,'add-staff.html',{'form':form})

def show1(request):
    member = Staff.objects.all()
    return render(request,"show1.html",{'member':member})
def edit(request, id):
    member =Staff.objects.get(id=id)
    return render(request,'edit.html', {'staff':member})
def update(request, id):
    member = Staff.objects.get(id=id)
    form = StaffForm(request.POST, instance = member)
    if form.is_valid():
        form.save()
        return redirect("/show1")
    return render(request, 'edit.html', {'member': member})
def destroy(request, id):
    member = Staff.objects.get(id=id)
    member.delete()
    return redirect("/show1")
