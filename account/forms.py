from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account

class DateInput(forms.DateInput):
    input_type = 'date'

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="E-mail", max_length=60, help_text="Unesite ispravnu E-mail adresu.")
    username = forms.CharField(label="Korisničko ime", max_length=30, help_text="Unesite jedinstveno korisničko ime.")

    class Meta:
        model = Account
        fields = ("username", "email", "gender", "date_of_birth", "password1", "password2")
        widgets = {
            'date_of_birth': DateInput()
        }


class AccountAuthenticationForm(forms.ModelForm):
    username = forms.CharField(label="Korisničko ime", max_length=30)
    password = forms.CharField(label='Lozinka', widget=forms.PasswordInput) 

    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Neispravno korisničko ime ili lozinka.')


class AccountUpdateForm(forms.ModelForm):
    email = forms.EmailField(label="E-mail", max_length=60)
    username = forms.CharField(label="Korisničko ime", max_length=30)

    class Meta:
        model = Account
        fields = ('username', 'email', 'gender', 'date_of_birth')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError("E-mail '%s' već postoji." % email)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError("Korisničko ime '%s' je već zauzeto." % username)