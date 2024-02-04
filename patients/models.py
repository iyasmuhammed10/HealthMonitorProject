from django.db import models

# Create your models here.

class User(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=50)


class Patients_Details(models.Model) :
    SEX_CHOICES = (
        ('male','male'),
        ('female', 'female'),
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number0 = models.IntegerField()
    phone_number1 = models.IntegerField()
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, default='male')
    device_ID = models.IntegerField()
    password = models.CharField(max_length=50)

    # IntegerField for id
    Doc_id = models.IntegerField(default=1)

    # IntegerField for id
    Hos_id = models.IntegerField(default=1)

    def __str__(self):
        return f'Patient Health - ID: {self.device_ID}'


class Patient_health(models.Model):
    heart_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    respiratory_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

