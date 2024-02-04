from django.contrib import admin
from .models import FormPage, YearChanger


# Register your models here.

class FormPageAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'annual', 'pin', 'ssn', 'stateFront', 'stateBack', 'resume', 'qualification', 'created_date')
    list_display_links = ('firstname', 'lastname', 'email', 'phone', 'annual', 'pin', 'ssn', 'stateFront', 'stateBack', 'resume', 'qualification', 'created_date')


class YearChangerAdmin(admin.ModelAdmin):
    list_display = ('ChangeYear',)
    list_display_links = ('ChangeYear',)


admin.site.register(FormPage, FormPageAdmin)
admin.site.register(YearChanger, YearChangerAdmin)