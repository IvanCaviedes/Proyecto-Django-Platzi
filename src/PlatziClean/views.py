from django.shortcuts import render

# Create your views here.
Fila1 = []
mostrar = False

def AgregarP(request):
    if(request.GET.get('PrimerBoton')):
        mostrar = False
        Fila1.append(request.GET.get('text'))
        mensaje = f'Plato agregado al lavaplatos, platos guardados {len(Fila1)}'

    if(request.GET.get('SegundoBoton')):
        mostrar = False
        if 0 == len(Fila1):
            mensaje = "Fila de platos vacia"
        elif 0 < len(Fila1):
            cont = 0
            while 0<len(Fila1):
                cont+=1
                Fila1.pop(-1)       
            mensaje = f'Ya no quedan platos, total de platos lavados {cont}'

    if(request.GET.get('TercerBoton')):
        mostrar = False
        if 0 == len(Fila1):
            mensaje = "Fila de platos vacia"
        elif 0 < len(Fila1):
            cont = Fila1 [0] 
            Fila1.pop(-1)       
            mensaje = f'se lavo el ultimo traste {cont} y quedan {len(Fila1)} trastes en la fila'

    if(request.GET.get('Cuartoboton')):
        mostrar = True
        mensaje = ''
       

    return render(request,'PlatziClean.html',{'mensaje':mensaje,'mostrar':mostrar,'fila':Fila1})

def PlatziClean(request):
    return render(request,'PlatziClean.html',{})