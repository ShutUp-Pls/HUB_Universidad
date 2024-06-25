import funcGrafo,func

def Cliques(nodo,grafo,cliq=[]):
    grafoMod,cliqMod = grafo[:],cliq[:]
    nodosNoRel = funcGrafo.NodosRelacionados(nodo,grafoMod,"norel")
    nodosRel = funcGrafo.NodosRelacionados(nodo,grafoMod,"rel")
    cliqMod.append(nodo)
    for n in nodosNoRel:
        grafoMod = funcGrafo.EliminarNodo(n,grafoMod)
    if ((len(cliqMod)*(len(cliqMod)-1))/2) != len(grafoMod):
        listaCliq = []
        for n in nodosRel:
            if not n in cliqMod:
                cliqModFin = Cliques(n,grafoMod,cliqMod)
                if func.EsListaDeListas(cliqModFin):
                    listaCliq.extend(cliqModFin)
                else:
                    listaCliq.append(cliqModFin)
        return listaCliq[:]
    else:
        return cliqMod[:]

def CliqueMaximo(grafo):
    nodosLista = funcGrafo.ListaNodos(grafo,True)
    listaCliques = []
    for n in nodosLista:
        listaCliques.extend(Cliques(n,grafo))
    cliqueMax = []
    for clique in listaCliques:
        if len(clique) > len(cliqueMax):
            cliqueMax = clique
    return cliqueMax