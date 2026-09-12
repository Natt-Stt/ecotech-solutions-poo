from registro_tiempo import RegistroTiempo


class Informe:
    def __init__(
        self,
        id_informe: int,
        titulo: str
    ):
        self.__id = id_informe
        self.titulo = titulo
        self.registros = []