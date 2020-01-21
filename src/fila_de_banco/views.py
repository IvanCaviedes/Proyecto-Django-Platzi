from django.shortcuts import render
import os


Fila1=[]
Fila2=[]
mostrar = False

def AgregarD(request):
    if(request.GET.get('PrimerBoton')):
        mostrar = False
        Fila1.append(request.GET.get('text'))
        mensaje = f'usuario agregado a fila de depósito, usuarios guardados {len(Fila1)}'


    if(request.GET.get('SegundoBoton')):
        mostrar = False
        Fila2.append(request.GET.get('text'))
        mensaje = f'usuario agregado a fila de apertura de cuenta, usuarios guardados {len(Fila2)}'



    if(request.GET.get('TercerBoton')):
        mostrar = False
        mensaje = 'tercer boton'



    if(request.GET.get('Cuartoboton')):
        mostrar = True
        mensaje = ''


    return render(request,'BanPlatzi.html',{'mensaje':mensaje,'fila':Fila1,'fila2':Fila2,'mostrar':mostrar});

def fila(request):
    return render(request,'BanPlatzi.html',{});
