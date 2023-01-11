from django import forms
from .models import Account



class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Enter password',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'confirm password',
        'class': 'form-control',
    }))

    class Meta:
        model = Account
        fields = ['username','email','mobile','password']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'enter username name'
        self.fields['mobile'].widget.attrs['placeholder'] = 'enter phone number'
        self.fields['email'].widget.attrs['placeholder'] = 'enter email'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password') 
        confirm_password = cleaned_data.get('confirm_password') 

        if password != confirm_password:
            raise forms.ValidationError(
                'password does not match!'
            )





class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username','mobile','email']
        

    def _init_(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super()._init_(*args, **kwargs)
        if instance is not None:
            self.instance = instance