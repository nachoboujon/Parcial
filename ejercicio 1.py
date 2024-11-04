class NodoArbol:
    def __init__(self, valor, datos):
        self.valor = valor
        self.datos = datos
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, datos):
        if not self.raiz:
            self.raiz = NodoArbol(valor, datos)
        else:
            self._insertarRecursivo(self.raiz, valor, datos)

    def _insertarRecursivo(self, nodo, valor, datos):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(valor, datos)
            else:
                self._insertarRecursivo(nodo.izquierda, valor, datos)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(valor, datos)
            else:
                self._insertarRecursivo(nodo.derecha, valor, datos)

    def buscar(self, valor):
        return self._buscarRecursivo(self.raiz, valor)

    def _buscarRecursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo
        elif valor < nodo.valor:
            return self._buscarRecursivo(nodo.izquierda, valor)
        else:
            return self._buscarRecursivo(nodo.derecha, valor)

    def buscarPorProximidad(self, prefijo):
        resultados = []
        self.busquedaProximidad(self.raiz, prefijo.lower(), resultados)
        return resultados

    def busquedaProximidad(self, nodo, prefijo, resultados):
        if nodo:
            if nodo.valor.lower().startswith(prefijo):
                resultados.append(nodo.datos)
            self.busquedaProximidad(nodo.izquierda, prefijo, resultados)
            self.busquedaProximidad(nodo.derecha, prefijo, resultados)

    def mostrarEnOrden(self):
        elementos = []
        self.ordenRecursivo(self.raiz, elementos)
        return elementos

    def ordenRecursivo(self, nodo, elementos):
        if nodo:
            self.ordenRecursivo(nodo.izquierda, elementos)
            elementos.append(nodo.datos)
            self.ordenRecursivo(nodo.derecha, elementos)

datosPokemon = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["planta", "veneno"]},
    {"nombre": "Ivysaur", "numero": 2, "tipo": ["planta", "veneno"]},
    {"nombre": "Venusaur", "numero": 3, "tipo": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipo": ["fuego"]},
    {"nombre": "Charmeleon", "numero": 5, "tipo": ["fuego"]},
    {"nombre": "Charizard", "numero": 6, "tipo": ["fuego", "volador"]},
    {"nombre": "Squirtle", "numero": 7, "tipo": ["agua"]},
    {"nombre": "Wartortle", "numero": 8, "tipo": ["agua"]},
    {"nombre": "Blastoise", "numero": 9, "tipo": ["agua"]},
    {"nombre": "Pikachu", "numero": 25, "tipo": ["eléctrico"]},
    {"nombre": "Raichu", "numero": 26, "tipo": ["eléctrico"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["eléctrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipo": ["roca", "dragón"]},
]

arbolNombre = ArbolBinario()
arbolNumero = ArbolBinario()
arbolTipo = ArbolBinario()

for pokemon in datosPokemon:
    arbolNombre.insertar(pokemon["nombre"], pokemon)
    arbolNumero.insertar(pokemon["numero"], pokemon)
    for tipo in pokemon["tipo"]:
        arbolTipo.insertar(tipo, pokemon)

# a) 
print("Árbol por nombre:", arbolNombre.mostrarEnOrden())
print("Árbol por número:", arbolNumero.mostrarEnOrden())
print("Árbol por tipo:", arbolTipo.mostrarEnOrden())

# b)
busquedaNombre = arbolNombre.buscar("Pikachu")
print("\nDatos de Pikachu:", busquedaNombre.datos if busquedaNombre else "No encontrado")

resultadosProximidad = arbolNombre.buscarPorProximidad("bul")
print("\nPokémon que comienzan con 'bul':", resultadosProximidad)

# c)
tiposInteres = ["agua", "fuego", "eléctrico"]
for tipo in tiposInteres:
    resultadosTipo = arbolTipo.buscar(tipo)
    if resultadosTipo:
        print(f"\nPokémon de tipo {tipo}:", resultadosTipo.datos)

# d)
print("\nListado por número:", arbolNumero.mostrarEnOrden())
print("Listado por nombre:", arbolNombre.mostrarEnOrden())

# e) 
for nombre in ["Jolteon", "Lycanroc", "Tyrantrum"]:
    pokemon = arbolNombre.buscar(nombre)
    print(f"\nDatos de {nombre}:", pokemon.datos if pokemon else "No encontrado")

# f)
contadorElectrico = len(arbolTipo.buscarPorProximidad("eléctrico"))
contadorAcero = len(arbolTipo.buscarPorProximidad("acero"))
print("\nCantidad de Pokémon de tipo eléctrico:", contadorElectrico)
print("Cantidad de Pokémon de tipo acero:", contadorAcero)
