from django.http import JsonResponse
from django.shortcuts import render
from .models import Credit, Client
from .forms import CreditForm, ClientForm
from django.db import IntegrityError

# Credits methods API
def show_credit(request):
    if request.method == 'GET':
        pass

def create_credit(request):
    try:
        if request.method == 'POST':
            client_form = ClientForm(request.POST)

            if client_form.is_valid():
                client_form.save()

            else:
                return JsonResponse({'status': '400', 'message': 'Verifiy personal data fields'}, safe=False)

            credit_form = CreditForm({
                    'credit_amount': request.POST['credit_amount'],
                    'comment': request.POST['comment'],
                    'client': Client.objects.get(dni=request.POST['dni'])
                })

            if not credit_form.is_valid():
                return JsonResponse({'status': '400', 'message': 'Verifiy credit amount field'}, safe=False)

            else:
                credit_form.save()

                return JsonResponse({
                        'status': '201', 
                        'message': 'Successfully created credit'}, safe=False)
                
    except:
        return JsonResponse({'status': '400', 'message': 'Bad request'}, safe=False)

def update_credit(request):
    if request.method == 'PUT':
        pass

def delete_credit(request):
    if request.method == 'DELETE':
        pass