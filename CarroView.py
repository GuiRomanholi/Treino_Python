from Carro import Carro
from CarroControl import CarroControl

class CarroView:
    def __init__(self):
        self.executando = True
        self.control = CarroControl()

    def sair(self):
        print("Até Breve!")
        self.executando = False
    
    def cadastro(self):
        c1 = Carro()
        c1.id = input("Digite o id: ")
        c1.marca = input("Digite a marca: ")
        c1.ano = int(input("Digite o ano: "))
        return self.control.salvar(c1)
    
    def pesquisa_por_nome(self):
        id = input("Digite o Carro que quer procurar: ")
        contato = self.control.pesquisando(id)
        print("Contato: ", contato)

    def menu(self):
        while self.executando:
            print("MENU - PRINCIPAL\n-(C)adastrar\n-(P)esquisar\n-(S)air")
            opcao = input("Informe a opcao desejada: ").upper()[0]
            if opcao == "C":
                self.cadastro()
            elif opcao == "P":
                self.pesquisa_por_nome()
            elif opcao == "S":
                self.sair()
            else:
                print("Por Favor Digite um Valor Válido")
