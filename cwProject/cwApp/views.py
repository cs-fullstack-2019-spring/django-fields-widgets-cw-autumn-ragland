from django.shortcuts import render, redirect
from .forms import SuperHeroForm
from django.http import HttpResponse


# render welcome page
def index(request):
    return render(request, 'cwApp/index.html')


# render form and save + redirect on submit
def application(request):
    form = SuperHeroForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('confirmation')

    context = {
        'form': form
    }
    return render(request, 'cwApp/application.html', context)


# render confirmation page
def confirmation(request):
    return render(request, 'cwApp/confirmation.html')
