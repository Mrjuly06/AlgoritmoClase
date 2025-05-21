class Nodo:
    def __init__(self,dato):
        self.dato=dato
        self.siguiente=None

#Definimos la clase tipo cola y sus metodos: Eliminar ,Insertar E Imprimir 
class Cola:
    def __init__(self,):
        self.frente=None
        self.final=None
#Metodo para insertar el elemento de la cola 
    def Insertar(Self,dato):
        nuevo=Nodo(dato)
        if self.final is None:
            self.frente=self,final=nuevo
            print(f"Elemento'{dato}' insertar")

#Metodo para elimirnar datos de la cola 
def Eliminar(self):
    if self.frente is None:
        print("La cola esta VAcia!!")
        return None 
    eliminado=self.frente.dato
    self.frente=self.frente.siguiente
    if self.frente is None:

# si la cola queda vacia 

         self.final=None
    print(f"Elemento" '{eliminado}' "eliminado")
    return eliminado
#Metod para imprimir la cola 
def imprimir(self):
    if self.frente is None:
        print("cola Vacia")
    else:
        print("contenido de la cola desded el frente al final")
        actual=self.frente
        while actual is None:
            print(altual.dato)
            actual=actual.siguiente
#julio\

      