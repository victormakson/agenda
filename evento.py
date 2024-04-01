class Evento:
    def __init__(self, titulo, data, hora, local):
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.local = local

    def __str__(self):
        return f"Título: {self.titulo}\nData: {self.data}\nHora: {self.hora}\nLocal: {self.local}\n"