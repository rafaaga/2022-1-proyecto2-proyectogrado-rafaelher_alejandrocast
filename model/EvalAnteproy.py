import json


class EvaluacionAnteproyecto:

    def __init__(self) -> None:
        super().__init__()
        self.criterios = {"planteamiento": [], "objetivos": [], "justificacion": [], "generales": [], "titulo": []}
        self.observaciones = ""
        self.nota = 0.0

        # Datos de toda evaluacion
        self.fecha_evaluacion = ""
        self.nombre_estudiante = ""
        self.id_estudiante = ""
        self.tema_proyecto = ""
        self.version_doc = " "  # Identifica la version en la que va la evaluación

        # Llamado al método que inicializa la información precargada
        self._inicializar_criterios()

    def _inicializar_criterios(self):
        # Criterios relacionados con el planteamiento
        # FIXME mover esta data para un json y hacer un método que cargue la data

        categoria = "Contexto"
        lista = []
        # lista.append(Criterio(categoria, "Introduce gradualmente al lector en el escenario donde se presenta el problema y describe características específicas que sean interesantes para entender la problemática (ejm geográficas, culturales, económicas)"))
        # lista.append(Criterio(categoria, "Presenta los involucrados en el proyecto (stakeholders) y la  información relevante para entender los stakeholders. Por ejemplo sus condiciones económicas, características culturales, étnicas, su forma de trabajo, etc ."))
        # lista.append(Criterio(categoria, "La información presentada en el contexto  es relevante para el problema"))
        # lista.append(Criterio(categoria, "Soporta el contexto con estudios, cifras, datos sectoriales de referencias bibliográficas de fuentes confiables. Ejm. estudios sectoriales, revistas o publicaciones académicas, medios de difusión nacional o internacional. NO: blogs, youtube, y fuentes no académicas"))
        self.criterios["planteamiento"] = lista

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

        # TODO completar con el resto de criterios
