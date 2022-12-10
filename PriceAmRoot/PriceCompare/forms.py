from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class UserCreation(UserCreationForm):
     class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']
    # username = forms.CharField(max_length=50)
    # email = forms.CharField(max_length=50)
    # password1 = forms.CharField(max_length=50)
    # password2 =forms.CharField(max_length=50)
    
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         User.objects.get(username=username)
    #         return username
    #     except User.DoesNotExist:
    #         raise forms.ValidationError("That username is not available.")
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     try:
    #         User.objects.get(email=email)
    #         return email
    #     except User.DoesNotExist:
    #         raise forms.ValidationError("That email is not available.")
    
    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if password1!= password2:
    #         raise forms.ValidationError("The two password fields didn't match.")
    #     return password2
    
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.username = self.cleaned_data['username']
    #     user.email = self.cleaned_data['email']
    #     user.set_password(self.cleaned_data['password1'])
    #     if commit:
    #         user.save()
    #         return user
    #     else:
    #         return user
    
       
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }
        # labels = {
        #     'username': 'Username',
        #     'email': 'Email',
        #     'password1': 'Password',
        #     'password2': 'Password',
        #     'remember_me': 'Remember me',
        # }


# class UserChangeForm(forms.ModelForm):
    # username = forms.CharField(max_length=50)
    # email = forms.CharField(max_length=50)
    # password1 = forms.CharField(max_length=50)
    # password2 = forms.CharField(max_length=50)
    
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']
    
    # def __init__(self, *args, **kwargs):
    #     super(UserChangeForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'
    
    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     try:
    #         User.objects.get(username=username)
    #         return username
    #     except User.DoesNotExist:
    #         raise forms.ValidationError("That username is not available.")
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     try:
    #         User.objects.get(email=email)
    #         return email
    #     except User.DoesNotExist:
    #         raise forms.ValidationError("That email is not available.")
    
    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #     if password1!= password2:
    #         raise forms.ValidationError("The two password fields didn't match.")
    #     return password2
    
    # def save(self, commit=True):
    #     user = super(UserChangeForm, self).save(commit=False)
    #     user.username = self.cleaned_data['username']
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #         return user
    #     else:
    #         return user
    
    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control'}),
    #         'email': forms.TextInput(attrs={'class': 'form-control'}),
    #         'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
    #         'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
    #                    'remember_me': forms.CheckboxInput(attrs={'class': 'form-control'}),
    #     }
    
    #     labels = {
    #         'username': 'Username',
    #         'email': 'Email',
    #         'password1': 'Password',
    #         'password2': 'Password',
    #                    'remember_me': 'Remember me',
    #     }


    
    
