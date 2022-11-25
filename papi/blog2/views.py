import math
import random
from urllib import request
from django.shortcuts import render
from .models import Datos

# Create your views here.

def muestra_datos(request):
    consulta= Datos.objects.all()
    listaSuma=calculaSuma(consulta)
    contexto= zip(consulta,listaSuma)
    return render(request, 'blog2/blog2.html', {'contexto':contexto})

def calculaSuma(l):
        listaSuma=[]
        for i in l:
            r=i.x1 + i.x3 + i.x4
            listaSuma.append(r)
        return listaSuma


#DISTANCIAEUCLIDIANA

def algKNN(request): 
    x1 = random.randint(1,500)
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    df = Datos.objects.all()
    ldis = distanciaEu(df,x1,x2,x3)
    ldis = sorted(ldis)
    contexto = zip(df,ldis)
    return render(request, 'blog2/algoritmo1.html', {'contexto':contexto})

def distanciaEu(df,x1,x2,x3):
    ldist = []
    for i in df:
        dis = (x1 - i.x1)**2+(x2 - i.x3)**2+(x3 - i.x4)**2
        raiz = round(math.sqrt(dis),4)
        ldist.append(raiz)
    return ldist


#BAYESIANO

def algBaye(request): 
    x1 = random.randint(1,500)
    x2 = random.randint(1,500)
    x3 = random.randint(1,500)
    df = Datos.objects.all()
    ldis = ABaye(df,x1,x2,x3)
    ldis = sorted(ldis)
    contexto = zip(df,ldis)
    return render(request, 'blog2/algoritmoBaye.html', {'contexto':contexto})

def ABaye(df,x1,x2,x3):
    ldist = []
    for i in df:
        dis = (x1 - i.x1)**2+(x2 - i.x3)**2+(x3 - i.x4)**2
        div = (dis / 27-1)
        ldist.append(div)
    return ldist

#RLineal
def RLineal(request):
    df = Datos.objects.all()
    ldis = Alineal(df)
    contexto = zip(df,ldis)
    return render(request, 'blog2/RAlineal.html', {'contexto':contexto})

def Alineal(df):
    ldist = []
    for i in df:
        sumx1= i.x1 + i.x3 + i.x4 
        sumx2= i.x1 + i.x3 + i.x4
        Tsum = sumx1 +sumx2
        media = 200
        Dsum = (Tsum /media)**2
        Dy =(i.x4 + i.x4)/2
        b =(Dy - Dsum)/media
        ldist.append(b)
    return ldist


