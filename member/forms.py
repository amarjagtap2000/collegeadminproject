from django import forms
from member.models import Staff
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = "__all__"






