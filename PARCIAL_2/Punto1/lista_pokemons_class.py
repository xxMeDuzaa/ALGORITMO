
class Pokemon:

    def __init__(
        self, 
        numero: int, 
        nombre: str, 
        tipos: list[str], 
        debilidades: list[str], 
        mega_evolucion: bool = False, 
        forma_gigamax: bool = False   
    ):
        self.numero = numero              
        self.nombre = nombre              
        self.tipos = tipos                # Lista de tipos (puede ser 1 o 2)
        self.debilidades = debilidades    # Lista de debilidades (frente a que tipo/tipos)
        self.mega_evolucion = mega_evolucion
        self.forma_gigamax = forma_gigamax

    def __str__(self):
        return (
            f'({self.numero}) {self.nombre} - Tipos: {self.tipos} - Debilidades: {self.debilidades}'
            f' | Mega: {"Sí" if self.mega_evolucion else "No"} | Gigamax: {"Sí" if self.forma_gigamax else "No"}'
        )