def UnirListas(lista1,lista2):
    listaUnir = lista1[:]
    for e in lista2:
        if not e in listaUnir:
            listaUnir.append(e)
    return listaUnir[:]

def RestarListas(lista1,lista2):
    listaResta = lista1[:]
    for e in lista2:
        if e in listaResta:
            listaResta.remove(e)
    return listaResta[:]

def EsListaDeListas(lista):
    for e in lista:
        if type(e) is list:
            return True
    return False