grafo: dict = {
    
}

def dfs(grafo=grafo, inicio="", objetivo="", visitados=None, camino=None, caminos_encontrados=None, i=0):
    i += 1

    # Si entramos a este método por primera vez
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    if caminos_encontrados is None:
        caminos_encontrados = []
    camino.append(inicio)
    visitados.add(inicio)
    if inicio == objetivo:
        caminos_encontrados.append(camino.copy())
    else:
        for vecino in grafo[inicio]:
            if vecino not in visitados:
                dfs(grafo, vecino, objetivo, visitados, camino, caminos_encontrados, i)

    camino.pop()  # Eliminamos el último nodo para retroceder al nodo anterior
    visitados.remove(inicio)

    return caminos_encontrados
