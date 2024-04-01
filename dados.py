from agendaeventos import AgendaEventos
from evento import Evento

agenda = AgendaEventos()

evento1 = Evento("Título 1", "01/01/2023", "10:00", "Local 1")
evento2 = Evento("Título 2", "02/01/2023", "14:00", "Local 2")
agenda.adicionar_evento(evento1)
agenda.adicionar_evento(evento2)

agenda.listar_eventos()

novo_evento = Evento("Novo Título", "01/01/2023", "10:00", "Local 1")
agenda.editar_evento(0, novo_evento)

agenda.listar_eventos()

agenda.remover_evento(1)

agenda.listar_eventos()