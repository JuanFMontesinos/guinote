class InvalidCard(Exception):
    """Excepción lanzada para errores en la entrada de la carta."""
    def __init__(self, message="La carta proporcionada no es válida"):
        super().__init__(message)