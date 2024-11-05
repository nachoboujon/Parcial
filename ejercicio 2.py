class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregarNodo(self, nodo):
        if nodo not in self.adyacencia:
            self.adyacencia[nodo] = {}

    def agregarConexion(self, nodo1, nodo2, episodios):
        if nodo1 in self.adyacencia and nodo2 in self.adyacencia:
            self.adyacencia[nodo1][nodo2] = episodios
            self.adyacencia[nodo2][nodo1] = episodios

    def mostrar(self):
        for nodo in self.adyacencia:
            print(f"{nodo}: {self.adyacencia[nodo]}")

    def episodiosCompartidos(self):
        episodiosMax = 0
        personajes = (None, None)

        for nodo1 in self.adyacencia:
            for nodo2, episodios in self.adyacencia[nodo1].items():
                if episodios > episodiosMax:
                    episodiosMax = episodios
                    personajes = (nodo1, nodo2)

        print(f"Máximo de episodios compartidos: {episodiosMax} entre {personajes[0]} y {personajes[1]}")

    def encontrarMST(self):
        aristas = []
        for nodo1 in self.adyacencia:
            for nodo2, episodios in self.adyacencia[nodo1].items():
                if (nodo2, nodo1, episodios) not in aristas:  
                    aristas.append((episodios, nodo1, nodo2))
        aristas.sort()  

        parent = {nodo: nodo for nodo in self.adyacencia}
        rank = {nodo: 0 for nodo in self.adyacencia}

        def find(nodo):
            if parent[nodo] != nodo:
                parent[nodo] = find(parent[nodo])
            return parent[nodo]

        def union(nodo1, nodo2):
            root1 = find(nodo1)
            root2 = find(nodo2)
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        mst = []
        for episodios, nodo1, nodo2 in aristas:
            if find(nodo1) != find(nodo2):
                union(nodo1, nodo2)
                mst.append((nodo1, nodo2, episodios))

        print("Árbol de Expansión Mínimo (MST):")
        for nodo1, nodo2, episodios in mst:
            print(f"{nodo1} -- {nodo2} (Episodios compartidos: {episodios})")

        return mst

    def contieneAYoda(self):
        mst = self.encontrarMST()
        personajes_en_mst = {nodo for arista in mst for nodo in arista[:2]}
        if "Yoda" in personajes_en_mst:
            print("El MST contiene a Yoda.")
        else:
            print("El MST no contiene a Yoda.")


grafoSW = Grafo()
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", 
    "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]
for personaje in personajes:
    grafoSW.agregarNodo(personaje)


grafoSW.agregarConexion("Luke Skywalker", "Leia", 4)
grafoSW.agregarConexion("Luke Skywalker", "Darth Vader", 3)
grafoSW.agregarConexion("Leia", "Han Solo", 3)
grafoSW.agregarConexion("Han Solo", "Chewbacca", 5)
grafoSW.agregarConexion("C-3PO", "R2-D2", 5)
grafoSW.agregarConexion("Yoda", "Luke Skywalker", 2)
grafoSW.agregarConexion("Rey", "BB-8", 3)
grafoSW.agregarConexion("Kylo Ren", "Rey", 2)
grafoSW.agregarConexion("Darth Vader", "Boba Fett", 1)
grafoSW.agregarConexion("Leia", "Chewbacca", 2)
grafoSW.agregarConexion("Han Solo", "Leia", 4)


grafoSW.mostrar()


grafoSW.episodiosCompartidos()


grafoSW.contieneAYoda()
