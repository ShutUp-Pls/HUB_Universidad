import funcGrafo,func

def RecubrimientosA(nodAr,grafo,recub=[]):
    recubMod = recub[:]
    if len(nodAr) == 1:
        listaRecub = []
        for relacion in grafo:
            if nodAr in relacion:
                recubFin = RecubrimientosA(relacion,grafo,recubMod[:])
                if func.EsListaDeListas(recubFin):
                    listaRecub.extend(recubFin)
                else:
                    listaRecub.append(recubFin)
        return listaRecub
    else:
        recubMod.append(nodAr)
        nodosGrafo = funcGrafo.ListaNodos(grafo,True)
        nodosRecub = funcGrafo.ListaNodos(recubMod,True)
        if len(nodosGrafo) != len(nodosRecub):
            listaRecub = []
            for n in nodosGrafo:
                if not n in nodosRecub:
                    recubFin = RecubrimientosA(n,grafo,recubMod[:])
                    if func.EsListaDeListas(recubFin):
                        listaRecub.extend(recubFin)
                    else:
                        listaRecub.append(recubFin)
            return listaRecub[:]
        else:
            return recubMod[:]

def RecubrimientoAMinimo(grafo):
    nodosLista = funcGrafo.ListaNodos(grafo,True)
    listaRecub = []
    for n in nodosLista:
        listaRecub.extend(RecubrimientosA(n,grafo))
    recubMin = nodosLista
    for recub in listaRecub:
        if len(recub) < len(recubMin):
            recubMin = recub
    return recubMin