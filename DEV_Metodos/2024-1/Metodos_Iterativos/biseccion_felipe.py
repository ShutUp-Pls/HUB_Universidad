import numpy as np
import biseccion as bs

def biseccion(a,b,TOL,fx,N):
    i = 1
    FA = fx(a)
    while (i<=N):
        p = a +(b-a)/2
       # print(p)
        FP = fx(p)
        if(FP == 0 or (b-a)/2 < TOL):
            return  print("resultado: ", p)
        
        tabla(i,N,a,b,p,fx(p))
        i+=1
        
        if (FA*FP > 0):
            a = p           
            FA = FP
        else: b = p  
    
    return print("El metodo fracaso depues de ", N, "iteraciones")

def tabla(i,N,a,b,p,fx):
    if(i==1):
         print(" i |", " a |",  " b |",  " p |", " f(p)")
         print("\n--------------------------------------------------\n")

    print(i,"  ", a, " ", b, " ", p, " ", fx)
        

TOL = 0.0001
N = 100
a = 1
b = 4
fx = lambda x:x**2-9
# biseccion(a,b,TOL,fx,N)
bs.print_ascii_table(bs.metodo_biseccion_descriptivo(fx,a,b,TOL,N))
