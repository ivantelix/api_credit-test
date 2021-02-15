from django.http import JsonResponse
from django.shortcuts import render
from .models import Credit
from .forms import CreditForm

# Credits methods API
def show_credit(request):
    if request.method == 'GET':
        pass

def create_credit(request):
    if request.method == 'POST':
        credit_form = CreditForm(request.POST)

        if credit_form.is_valid():
            if float(request.POST['credit_amount']) <= 50000:
                credit_form.save()

                return JsonResponse({
                        'status': '201', 
                        'message': 'Successfully created credit'}, safe=False)
            
            else:
                return JsonResponse({
                    'status': '400', 
                    'message': 'Credit amount exceded limit of $50.000,00'}, safe=False)

        else:
            return JsonResponse({'status': '400', 'message': 'Bad request'}, safe=False)

def update_credit(request):
    if request.method == 'PUT':
        pass

def delete_credit(request):
    if request.method == 'DELETE':
        pass