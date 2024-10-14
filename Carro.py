
class Carro:

    def __init__(self,id: str = "",marca: str = "", ano: int = 0):
        self.id = id
        self.marca = marca
        self.ano = ano
    
    def dicionario(self) -> dict:
        dic= {
            "id": self.id,
            "marca": self.marca,
            "ano": self.ano
        }
        return dic

    def __str__(self):
        return f"ID: {self.id}\nMarca: {self.marca}\nAno: {self.ano}"