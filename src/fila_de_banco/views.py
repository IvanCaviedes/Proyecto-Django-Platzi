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

        if 0 == len(Fila1) and 0 == len(Fila2):
            mensaje = "Filas vacias por favor ingrese datos"
        elif 0 == len(Fila1) and 0<len(Fila2):
            cont =0
            while 0<len(Fila2):
                cont+=1
                Fila2.pop(0)       
            mensaje = f'Usuarios atendidos de la fila Apertura {cont}'

        elif 0<len(Fila1) and 0 ==len(Fila2):
            cont =0
            while 0<len(Fila1):
                cont+=1
                Fila1.pop(0)       
            mensaje = f'Usuarios atendidos de la fila Deposito {cont}'
        elif 0 < len(Fila1) and 0 < len(Fila2):
            hola = True
            cont = 0
            cont1 = 0
            while hola:
                if 0<len(Fila1):
                    cont+=1
                    Fila1.pop(0)
                elif 0<len(Fila2):
                    cont1+=1
                    Fila2.pop(0)
                else:
                    mensaje = f'se han atendido los clientes de las dos filas, fila Depocito {cont} clientes y fila Apertura {cont1} clientes'
                    hola = False       

    if(request.GET.get('Cuartoboton')):
        mostrar = True
        mensaje = ''


    return render(request,'BanPlatzi.html',{'mensaje':mensaje,'fila':Fila1,'fila2':Fila2,'mostrar':mostrar});

def fila(request):
    return render(request,'BanPlatzi.html',{});
