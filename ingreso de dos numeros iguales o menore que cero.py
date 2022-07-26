# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:39:19 2022

@author: lab
"""
cont=0
a=0
b=0
prom=0
prom_1=0
while True:
  while True:
      cont=cont+1
      x=int(input("Ingrese un número: "))
      y=int(input("Ingrese un número: "))
      if x<1 or y<1:
          a=a+1
          print("los numeros son menores que 0 , vuelva a ingresar ")  
      elif x==y:
          b=b+1
          print("los numeros son iguales , vuelva a ingresar ")     
      else: 
          break
  salir=input("para salir digite salir: ")
  if salir=='salir' or salir=='Salir' or salir=='SALIR':
      print(" el número de veces que se digito menores que 0 : ",a)
      print(" el número de veces que se digito numeros iguales es : ",b)
      print(" el número de veces que se a ejecuado el programa es : ",cont)
      prom=a/cont
      prom_1=b/cont
      print("el promedio número negativos: ",prom)
      print("el promedio números igualess: ",prom_1)
      break
 