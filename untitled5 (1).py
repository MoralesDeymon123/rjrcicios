# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 14:31:32 2022

@author: lab
"""

def keyw (**datos):
    print("\n Tipo de datos de argumentto:",type(datos))
    
    for key, value in datos.items():
        print("{}es {}".format(key, value))
        keyw(Primernombre="Jhon",
             Apellido="Ruiz",
             Age=42
             Telefono=123456)
        