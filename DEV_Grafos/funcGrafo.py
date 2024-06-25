def ListaNodos(grafo,ordenar=False):
    nodos = []
    for relacion in grafo:
        for nodo in relacion:
            if nodo not in nodos:
                nodos.append(nodo)
    if ordenar == True:
        nodos.sort()
    return nodos[:]

def GradoNodos(grafo,var=None):
    if var == "dicc" or var is None:
        nodos = ListaNodos(grafo,True)
        diccionario = {}
        for nodo in nodos:
            diccionario[nodo] = GradoNodos(grafo,nodo)
        return diccionario
    elif var == "list":
        nodos = ListaNodos(grafo,True)
        lista = []
        for nodo in nodos:
            lista.append(GradoNodos(grafo,nodo))
        return lista[:]
    else:
        grado = 0
        for relacion in grafo:
            if var in relacion:
                grado += 1
        return grado

def NodosRelacionados(nodo,grafo,retorna=None):
    nodoOut = ListaNodos(grafo)
    nodoOut.remove(nodo)
    nodoIn = []
    for relacion in grafo:
        if nodo in relacion:
            for n in relacion:
                if n != nodo and not n in nodoIn:
                    nodoIn.append(n)
                    nodoOut.remove(n)
    if retorna == "rel" or retorna is None:
        return nodoIn[:]
    if retorna == "norel":
        return nodoOut[:]

def RelacionesNodo(nodo,grafo,retorna=None):
    listaRelaciones = []
    listaNoRelaciones = grafo[:]
    for relacion in grafo:
        if nodo in relacion:
            listaRelaciones.append(relacion)
            listaNoRelaciones.remove(relacion)
    if retorna == "rel" or retorna is None:
        return listaRelaciones
    if retorna == "norel":
        return listaNoRelaciones

def EliminarNodo(nodo,grafo):
    grafoMod = grafo[:]
    for relacion in grafo:
        if nodo in relacion:
            grafoMod.remove(relacion)
    return grafoMod[:]

def RadioEspectral(grafo):
    gradosNodos = GradoNodos(grafo,"list")
    radioEspectral = []
    for i in range(len(gradosNodos)):
        radioEspectral.append(gradosNodos.count(i))
    return radioEspectral[:]