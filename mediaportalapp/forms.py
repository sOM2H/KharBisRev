# -- coding: utf-8 --

from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):

    """
       Form for login on site, 
       checks if the entered user
       login exists in the system 
       and whether the entered password matches it
    """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
   
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователя с таким логином не существует!')
        
        user = User.objects.get(username=username)
        
        if not user.check_password(password):
            raise forms.ValidationError('Неверный пароль!')
       

User = get_user_model()


class RegistrationForm(forms.ModelForm):

    """Check if entered username in system already exist
     and match up of passwords"""

    password_check = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_check'
        ]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['password_check'].label = 'Подтвердите пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует!')
        
        if password != password_check:
            raise forms.ValidationError('Ваши пароли не совпадают!')