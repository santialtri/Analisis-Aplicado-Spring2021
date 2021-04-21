# -*- coding: utf-8 -*-
"""AnálisisAplicadoParcial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AbFG1G_xe-pMn5FZnTIyWzV4v0oy749U
"""

def Rosen (i,k,a,b):
      z = (a-i)**2 + b*(k-i**2)**2
  return z

def BusquedaLineal_amplio(f, x0, metodo="maximo descenso"):
    xk=x0
    if metodo == "Newton":
        while not (f_o_c(f,xk)) and (s_o_c(f,xk)):
            grad=Grad(f, xk)
            hess=Hess(f,xk)
            pk=LA.solve(hess,-grad)
            alpha = genera_alpha(f,x0,pk)
            xk= xk + alpha*pk
    else:
        while not (f_o_c(f,xk)) and (s_o_c(f,xk)):
            grad=Grad(f,xk)
            pk = -grad
            alpha = genera_alpha(f,xk,pk)
            xk = xk + alpha*pk
    return xk

x = list(range(100))
y = list(range(100))

BusquedaLineal_amplio(f(x,y), xk, "Newton")