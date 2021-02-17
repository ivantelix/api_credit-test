from django.contrib import admin
from .models import Client, Credit

# Register your models here.
class CreditAdminLine(admin.TabularInline):
    model = Credit
    fields = ('credit_amount', 'comment', 'client')

class ClientAdmin(admin.ModelAdmin):
    model = Client
    fields = ('names', 'dni', 'date_birthday')
    inlines = [CreditAdminLine]

    list_display = ('names', 'dni')


admin.site.register(Client, ClientAdmin)