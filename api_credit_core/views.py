from django.http import JsonResponse, HttpResponse
from .models import Credit, Client
from .forms import CreditForm, ClientForm
from django.db import IntegrityError
from django.core import serializers
from django.views import View


# Credits methods API
class CreditView(View):
    def get(self, request):
        if request.method == 'GET':
            if 'id' in request.GET:
                data = Credit.objects.filter(id=request.GET['id'])
            else:   
                data = Credit.objects.all()

            return JsonResponse(list(data.values()), safe=False)
        
    
    def post(self,request):
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

    def put(self, request):
        pass

    def delete(self, request):
        pass