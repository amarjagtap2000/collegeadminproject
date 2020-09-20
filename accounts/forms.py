from django import forms
from accounts.models import Account,Result
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = "__all__"








