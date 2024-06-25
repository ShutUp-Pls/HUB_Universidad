import funcGrafo,func

def Cuplajes(relacion,grafo,cuplaje=[]):
    grafoMod,cuplajeMod = grafo[:],cuplaje[:]
    cuplajeMod.append(relacion)
    for n in relacion:
        grafoMod = funcGrafo.EliminarNodo(n,grafoMod)
    if len(grafoMod) != 0:
        listaCuplaje = []
        for rel in grafoMod:
            cuplajeFin = Cuplajes(rel,grafoMod,cuplajeMod)
            if func.EsListaDeListas(cuplajeFin):
                listaCuplaje.extend(cuplajeFin)
            else:
                listaCuplaje.append(cuplajeFin)
        return listaCuplaje[:]
    else:
        return cuplajeMod[:]

def CuplajeMaximo(grafo):
    listaCuplajes = []
    for r in grafo:
        listaCuplajes.extend(Cuplajes(r,grafo))
    cuplajeMax = []
    for cuplaje in listaCuplajes:
        if len(cuplaje) > len(cuplajeMax):
            cuplajeMax = cuplaje
    return cuplajeMax