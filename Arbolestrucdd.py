import graphviz

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def construir_arbol(lista):
    """
    construir un árbol binario completo (por nivel) a partir de una lista.
    """
    if not lista:
        return None

    # crear un nodo por cada valor
    nodos = [Nodo(valor) for valor in lista]
    n = len(nodos)
    
    # asignar los hijos en base a la notación de arreglo de árbol completo
    for i in range(n):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < n:
            nodos[i].izquierda = nodos[left_index]
        if right_index < n:
            nodos[i].derecha = nodos[right_index]
    
    return nodos[0]  # la raíz se encuentra en la posición 0

def visualizar_arbol(raiz):
    """
    Genera una visualización del árbol utilizando Graphviz.
    """
    dot = graphviz.Digraph(comment="Árbol Completo del PDF")
    
    def agregar_nodos(nodo):
        if nodo:
            # crear nodo en Graphviz con el valor del nodo actual
            dot.node(str(nodo.valor))
            if nodo.izquierda:
                dot.edge(str(nodo.valor), str(nodo.izquierda.valor))
                agregar_nodos(nodo.izquierda)
            if nodo.derecha:
                dot.edge(str(nodo.valor), str(nodo.derecha.valor))
                agregar_nodos(nodo.derecha)
    
    agregar_nodos(raiz)
    dot.render("Arbol_documento", format="png", view=False)  # se guarda como Arbol_documento.png

# lista de valores según el archivo ARBOL.pdf  
valores = [20, 15, 24, 12, 17, 14, 44, 9, 16, 11, 23, 10, 27, 25, 50]

# construir el árbol (suponiendo que la lista está en orden de nivel)
raiz = construir_arbol(valores)

# visualizar el árbol generado
visualizar_arbol(raiz)
