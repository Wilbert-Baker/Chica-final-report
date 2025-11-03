from django import forms
from . models import Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    class UserLoginForm(AuthenticationForm):
        username = forms.CharField(label="Username", max_length=100)
        password = forms.CharField(label="Password", widget=forms.PasswordInput)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 3, "placeholder": "write your commt here..."})
        }
        class ContactAdminForm(forms.Form):
          subject = forms.CharField(max_length=100)
          message = forms.CharField(widget=forms.Textarea)

        

        