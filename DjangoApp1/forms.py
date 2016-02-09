from django import forms
from django.contrib.auth.models import User
from DjangoApp1.models import UserProfile, Tapas

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class TapaForm(forms.ModelForm):
    nombre = forms.CharField (max_length=15, label= "Name of the Tapa")
    
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapas
        exclude = ('bar',)
        fields = ('nombre', 'picture')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

