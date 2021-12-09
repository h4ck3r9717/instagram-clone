
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse,reverse_lazy
from users.forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect
@csrf_protect
def register(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'home/index.html')
    context['form']=form
    return render(request,'registration/register.html',context)


#followers