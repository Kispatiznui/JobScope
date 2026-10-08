class JobScopeException(Exception):
    """Error base de JobScope."""


class SourceError(JobScopeException):
    """Error al obtener información de una fuente de empleos."""


class ConfigurationError(JobScopeException):
    """Error en la configuración de JobScope."""