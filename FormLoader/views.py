from django.shortcuts import render, HttpResponse
from .form import FormPageForm
from .models import YearChanger


# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    ChangeYear = YearChanger.objects.values_list('ChangeYear', flat=True).distinct()
    data = {
        'ChangeYear': ChangeYear,
    }
    return render(request, "about.html", data)

def values(request):
    return render(request, "values.html")

def awards(request):
    return render(request, "awards.html")

def application(request):
    if request.method == 'POST':
        form = FormPageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Your application is submitted and under review. We would reach out to you once it is reviewed')
        else:
            context = {'forms': FormPageForm()}
            return render(request, 'application.html', context)
    context = {'form': FormPageForm()}
    return render(request, "application.html", context)

def vacancy(request):
    return render(request, 'vacancy.html')


