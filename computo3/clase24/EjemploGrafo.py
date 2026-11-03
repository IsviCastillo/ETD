class Grafo:
    def __init__((self)):
        self.adyacencia = {}

    def agregar_vertice(self,vertices):
        for vertice in vertices:
            if vertice not in self.adyacencia:
                self.adyacencia[vertice]=[]    

    def agregar_arista(self, origen, desrino):
        self.agregar_arista(origen)
        self.agregar_arista(destino)
        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)
            self.adyacencia[destino].append(origen)

            if origen not in self.adyacencia[destino]:
                self.adyacencia[destino].append(origen)
                