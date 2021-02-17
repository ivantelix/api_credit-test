from django.db import models

# Create your models here.
class Client(models.Model):
    names = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    date_birthday = models.DateField()

class Credit(models.Model):
    #names = models.CharField(max_length=100)
    #last_name = models.CharField(max_length=100)
    #dni = models.CharField(max_length=20)
    credit_amount = models.FloatField()
    comment = models.CharField(max_length=250, null=True, blank=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = "credit"
        verbose_name_plural = "credits"
