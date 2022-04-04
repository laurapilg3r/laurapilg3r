from Funcionarios import Funcionario
from Valores import valores 

gerson = Funcionario(nome="Gerson Ataide")
jorge = Funcionario(nome="Jorge Santos")

gerson.imprime_dados_cliente()
jorge.imprime_dados_cliente()

conta_gerson = (gerson, 2000)
conta_jorge = (jorge, 2001)