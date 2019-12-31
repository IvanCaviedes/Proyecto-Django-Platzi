from django.shortcuts import render
from .forms import banco
import os
# Create your views here.
def fila(request):
    form = banco(request.POST or None)
    if form.is_valid():
        form_data = form.cleaned_data
        Datos = form_data.get('Datos')
        return render(request,'BanPlatzi.html',{'salida':Datos});
    return render(request,'BanPlatzi.html',{'form':form});
