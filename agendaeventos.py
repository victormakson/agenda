from evento import Evento

class AgendaEventos:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, evento):
        self.eventos.append(evento)

    def editar_evento(self, indice, novo_evento):
        self.eventos[indice] = novo_evento

    def remover_evento(self, indice):
        self.eventos.pop(indice)

    def listar_eventos(self):
        for evento in self.eventos:
            print(evento)