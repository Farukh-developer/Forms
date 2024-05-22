from django.shortcuts import render

from .forms import AdminstratorForm, Studentform


def home(request):
    if request.method=='POST':
        form=AdminstratorForm(data=request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form=AdminstratorForm()
    
    form=AdminstratorForm()        
    
    context={
        "form":form
    }
    return render(request, 'home.html', context)

#####################################

def index(request):
    if request.method=='POST':
        form=Studentform(data=request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form=Studentform()
    
    form=Studentform()        
    
    context={
        "form":form
    }
    return render(request, 'home.html', context)