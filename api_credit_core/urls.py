from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('show/', views.CreditView.as_view()),
    #path('search/<int:cod_credit>', views.show_credit),
    path('create/', views.CreditView.as_view()),
    #path('update/<int:cod_credit>', views.update_credit),
    #path('delete/<int:cod_credit>', views.delete_credit),
]
