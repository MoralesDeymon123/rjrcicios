# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 08:35:46 2022

@author: lab
"""

#Matriz inversa
import random

c = int(-1)

n=int(input("Favor ingresar el valor de n:"))
vec=[None] * n * n

matriz=[None] * n
for i in range(0,n):
    for j in range(0,n):
        matriz[i][j] = (int)(random.randint(1,1001))
        
for i in range(n - 1,  -1,  -1):
    for j in range(n - 1,  -1,  -1):
        c = c+1;
        vec[c]=matriz[i][j]
        
print(vec)
#Metodo Gauss y Gauss Jordan

Matriz =[]
res=[]

def mat(n):
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)
    return matriz

def llenar(n):
    matriz= mat(n)
    for x in range(n):
        matriz[x][y]=float(input("Valor de [" + srt(x) + "]["srt(y) + ="] ="))
    res.append(float(input("Valor del resultado de la matriz [" + srt(x) +"] =")))


def gauss(n):
    for z in range (n-1):                                                                           
        for x in range(1, n-z):
            if (matriz[z][z] !=0 ):
                p = matriz[x+z][z] /matriz[z][z]
                for y in range (n):
                    matriz[x+z][z]=matriz[x+z][z] - (matriz[z][y]*p)
                res[x+z] = res[x+z] -(res[z]*p)
                
def gjordan(n):
    for z in range (n-1, 0,-1):
        for x in range(z):
            if (matriz[z][z] !=0):
               p = matriz[x][z]/matriz[z][z]
               matriz[x][z] = matriz[x][z] -(matriz[z][z]*p)
               res[x]= res[x] - (res(z)*p)

                
def sol(n):
    for i in range(n):
        if(matriz[i][i] !=0):
           ms=True
        else:
            ms= False
            break
    if(ms==True):
        for i in range (n):
            print("El valor  de x" + srt(i) +"es =" +srt(res[i]/matriz[i][i])
    else:
        print("La matriz no tiene solucion")
        
def det(n):
    deter=1
    for x in range(n):
        deter=matriz[x][x]*deter
    print"/nEl determinante de la matriz es = ",deter

def in(n):
    for i in range(n):
        for j in range(n):
            print matriz[i][j]
        print "/n"