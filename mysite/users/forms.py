from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class newUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'example@gmail.com'}))
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'focus:outline-none','placeholder':'john'}))
    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    password2 = forms.CharField( max_length=100, required=True, widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))

    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self,commit=True):
        user = super(newUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user