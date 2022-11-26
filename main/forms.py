from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['kurs', 'group']
        widgets = {
            'kurs': forms.TextInput(attrs={'class': 'name', 'id': "kurs", 'type': "text"}),
            'group': forms.TextInput(attrs={'class': 'password', 'id': "group", 'type': "text"}),
        }

        # 'kurs': forms.HiddenInput(),