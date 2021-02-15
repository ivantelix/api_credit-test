from django import forms
from .models import Credit

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['names', 'last_name', 'dni', 'credit_amount', 'comment']