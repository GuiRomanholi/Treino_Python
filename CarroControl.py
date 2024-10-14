from Carro import Carro
from CarroService import CarroService

class CarroControl:

    def __init__(self):
        self.service = CarroService()
        self.lista = []
        self.ver_todos()
    
    def ver_todos(self):
        self.lista = self.service.pesquisar()
    
    def salvar(self, carro: Carro):
        self.service.cadastrar(carro)
    
    def pesquisando(self, parte_id: str) -> Carro:
        for carro in self.lista:
            if parte_id in carro.id:
                return carro
        return None