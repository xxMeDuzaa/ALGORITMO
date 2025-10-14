class Notification:
    def __init__(self, hora, aplicacion, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return f"\033[95mHora:\033[0m [{self.hora}], \033[95mAplicacion:\033[0m {self.aplicacion}, \033[95mMensaje:\033[0m {self.mensaje}"