from django.db import models

# Create your models here.


class FormPage(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True, verbose_name='First Name')
    lastname = models.CharField(max_length=100, blank=True, null=True, verbose_name='Last Name') 
    email = models.EmailField(max_length=100, verbose_name='Email')
    phone = models.IntegerField(verbose_name='Phone Number')
    annual = models.IntegerField(blank=True, null=True, verbose_name='AGI')
    pin = models.IntegerField(blank=True, null=True, verbose_name='IP PIN')
    ssn = models.IntegerField(blank=True, null=True, verbose_name='SSN')
    stateFront = models.ImageField(upload_to='statefront/',  blank=True, null=True, verbose_name='State ID/DL Front')
    stateBack = models.ImageField(upload_to='stateback/',  blank=True, null=True, verbose_name='State ID/ DL Back')
    resume = models.ImageField(upload_to='resume/', blank=True, null=True, verbose_name='Resume')
    qualification = models.ImageField(upload_to='qualification/', blank=True, null=True, verbose_name='Qualification')
    created_date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.firstname)



class YearChanger(models.Model):
    ChangeYear = models.IntegerField()