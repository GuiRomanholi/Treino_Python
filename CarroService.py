import json
import requests
from Carro import Carro


class CarroService:
    def __init__(self):
        self.URL_BASE = "https://dtspm-327f2-default-rtdb.firebaseio.com"
    
    def cadastrar(self, carro: Carro) -> bool:
        response = requests.post(url=f"{self.URL_BASE}/carros.json", json=carro.dicionario(), timeout=5.0)
        return response.status_code == 200
    
    def pesquisar(self) -> list:
        response = requests.get(url=f"{self.URL_BASE}/carros.json", timeout=5.0)
        lista = []
        if response.status_code == 200:
            dicionario = json.loads(response.text)
            if dicionario:
                for item in dicionario.items():
                    carro_dict = item[1]
                    c1 = Carro(id=carro_dict.get("id",""),
                               marca=carro_dict.get("marca",""),
                               ano=carro_dict.get("ano", 0))
                    lista.append(c1)
        return lista