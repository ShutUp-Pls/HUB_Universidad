import funcGrafo,func

def Recubrimientos(nodo,grafo,recub=[]):
    recubMod = recub[:]
    recubMod.append(nodo)
    grafoMod = funcGrafo.EliminarNodo(nodo,grafo)
    if len(grafoMod) != 0:
        nodosLista = funcGrafo.ListaNodos(grafoMod)
        recubLista = []
        for n in nodosLista:
            recubFin = Recubrimientos(n,grafoMod,recubMod)
            if func.EsListaDeListas(recubFin):
                recubLista.extend(recubFin)
            else:
                recubLista.append(recubFin)
        return recubLista[:]
    else:
        return recubMod[:]

def RecubrimientoMinimo(grafo):
    nodosLista = funcGrafo.ListaNodos(grafo,True)
    listaRecub = []
    for n in nodosLista:
        listaRecub.extend(Recubrimientos(n,grafo))
    recubMin = nodosLista
    for recub in listaRecub:
        if len(recub) < len(recubMin):
            recubMin = recub
    return recubMin