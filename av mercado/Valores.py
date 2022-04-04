class valores:
    
    def __init__(self, vendas=0, numero="001"):
        self.vendas = vendas
        self.numero = numero
        
    def resumo(self):
        print(f"Numero de funcionario: {self.numero}\nVendas: {self.vendas}")
        
    def bonus(self,vendas):
            
            porcentagem = 100%(vendas*8)
            bonus_total = porcentagem + vendas
            print("o bonus desse funcionario é {}, totalizando com seu salario é {}".format(porcentagem, bonus_total))
        

