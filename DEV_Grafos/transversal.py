import funcGrafo,func

def PresionarNodo(nodo,grafo,pres=[]):
    presMod = pres[:]
    if not nodo in presMod:
        presMod.append(nodo)
        nodosRel = funcGrafo.NodosRelacionados(nodo,grafo,"rel")
        presMod = func.UnirListas(presMod,nodosRel)
    else:
        print("Nodo ya fué presionado")
    return presMod[:]

def Transversales(nodo,grafo,trans=[],nodosPres=[]):
    transMod,nodosPresMod = trans[:],nodosPres[:]
    transMod.append(nodo)
    nodosPresMod = PresionarNodo(nodo,grafo,nodosPresMod)
    nodosLista = funcGrafo.ListaNodos(grafo)
    if len(nodosPresMod) != len(nodosLista):
        listaDeTrans = []
        nodosDisp = func.RestarListas(nodosLista,nodosPresMod)
        for n in nodosDisp:
            transFin = Transversales(n,grafo,transMod,nodosPresMod)
            if func.EsListaDeListas(transFin):
                listaDeTrans.extend(transFin)
            else:
                listaDeTrans.append(transFin)
        return listaDeTrans[:]
    else:
        return transMod[:]

def TransversalMinimo(grafo):
    nodosLista = funcGrafo.ListaNodos(grafo,True)
    listaTrans = []
    for n in nodosLista:
        listaTrans.extend(Transversales(n,grafo))
    transMin = nodosLista
    for trans in listaTrans:
        if len(trans) < len(transMin):
            transMin = trans
    return transMin