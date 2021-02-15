from django import forms
from .models import Credit, Client

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = '__all__'
        #fields = ['names', 'last_name', 'dni', 'credit_amount', 'comment']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def save_custom(self, client):
        client = self.save(commit=False)
        return 1
        
