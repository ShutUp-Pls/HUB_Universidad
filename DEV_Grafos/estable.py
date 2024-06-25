import funcGrafo,transversal

def EstableMaximo(grafo):
    nodosLista = funcGrafo.ListaNodos(grafo,True)
    listaEstables = []
    for n in nodosLista:
        listaEstables.extend(transversal.Transversales(n,grafo))
    estableMax = []
    for estable in listaEstables:
        if len(estable) > len(estableMax):
            estableMax = estable
    return estableMax