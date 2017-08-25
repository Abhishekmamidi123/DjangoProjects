from appTwo.models import User
from django import forms

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
