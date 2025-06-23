'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

from interface.interface_aprova import AprovacaoExame

class Exame:
    def __init__(self, tipo, dados):
        self.tipo = tipo
        self.dados = dados

class AprovadorExameSangue(AprovacaoExame):
    def aprovar(self, exame):
        if exame.dados.get('hemoglobina') > 13:
            print("Exame de sangue aprovado!")
        else:
            print("Exame de sangue reprovado!")

class AprovadorRaioX(AprovacaoExame):
    def aprovar(self, exame):
        if exame.dados.get("imagem_boa"):
            print("Raio X aprovado!")
        else:
            print("Raio X reprovado!")

class SistemaAprovador:
    def __init__(self):
        self.aprovadores = {}

    def registro_aprovador(self, tipo_exame, aprovador: AprovacaoExame):
        self.aprovadores[tipo_exame] = aprovador

    def aprovar_exame(self, exame: Exame):
        aprovador = self.aprovadores.get(exame.tipo)
        if aprovador:
            aprovador.aprovar(exame)
        else: 
            print(f"Nenhum aprovador encontrado para o tipo: {exame.tipo}")

sistema = SistemaAprovador()
sistema.registro_aprovador("sangue", AprovadorExameSangue())
sistema.registro_aprovador("raio x", AprovadorRaioX())

exameSangue = Exame("sangue", {"hemoglobina": 11})
exameRaioX = Exame("raio x", {"imagem_boa": True})

sistema.aprovar_exame(exameSangue)
sistema.aprovar_exame(exameRaioX)