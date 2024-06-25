import funcGrafo,transversal,recubrimiento,estable,clique,recubrimientoA,cuplaje

#G = ["ab","bc","cd","dg","gf","fe","ea","ec","bg"]
#G = ["12","24","46","65","53","31","25","34"]
#G = ["12","24","46","65","53","31","25","63"]
#G = ["12","23","36","35","25","14","45","47","57"]

#(Ejercicio de Comparación)
G = ["14","43","35","52","21","23","24"]
#G = ["12","24","45","53","34","41","15"]

P = 1 #Componentes conexas 

def Invariantes(grafo):
    n = len(funcGrafo.ListaNodos(grafo))
    m = len(grafo)
    p = m-n+P
    d = funcGrafo.RadioEspectral(grafo)
    delta = transversal.TransversalMinimo(grafo)
    alpha = recubrimiento.RecubrimientoMinimo(grafo)
    beta = estable.EstableMaximo(grafo)
    betap = clique.CliqueMaximo(grafo)
    alphae = recubrimientoA.RecubrimientoAMinimo(grafo)
    betae = cuplaje.CuplajeMaximo(grafo)
    return n,m,p,d,delta,alpha,beta,betap,alphae,betae

def main():
    n,m,p,d,delta,alpha,beta,betap,alphae,betae = Invariantes(G)
    print("1) Nº de Nodos:",n)
    print("2) Nª de Aristas:",m)
    print("3) Nº de componentes conexas:",P)
    print("4) Rango de Ciclo:",p)
    print("5) Radio Espectral:",d)
    print("6) Transversal minimo:", delta, "Tamaño:", len(delta))
    print("7) Recubrimiento minimo:", alpha, "Tamaño:", len(alpha))
    print("8) Estable maximo:", beta, "Tamaño:", len(beta))
    print("9) Clique maximo:", betap, "Tamaño:", len(betap))
    print("10) Recubrimiento de Aristas Minimo:", alphae, "Tamaño:", len(alphae))
    print("11) Cuplaje maximo:", betae, "Tamaño:", len(betae))

main()