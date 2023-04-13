#################################iNSCRIPCION#######################################
from jc_python_flask.Modelos.Inscripcion import Inscripcion
from jc_python_flask.Repositorios.RepositorioInscripcion import RepositorioInscripcion


"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInscripcion():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        print("Creando ControladorInscripcion")
        self.repositorioInscripcion = RepositorioInscripcion()

    def index(self):
        print("Listar todos las inscripciones")
        return self.repositorioInscripcion.findAll()

    def create(self, laInscripcion):
        print("Crear una inscripcion")
        nuevaInscripcion = Inscripcion(laInscripcion)
        return self.repositorioInscripcion.save(nuevaInscripcion)

    def show(self, id):
        print("Mostrando una inscripcion con id ", id)
        laInscripcion = Inscripcion(self.repositorioInscripcion.findById(id))
        return laInscripcion.__dict__

    def update(self, id, laInscripcion):
        print("Actualizando inscripcion con id ", id)
        inscripcionActual = Inscripcion(self.repositorioInscripcion.findById(id))
        inscripcionActual.año = laInscripcion["año"]
        inscripcionActual.semestre = laInscripcion["semestre"]
        inscripcionActual.nota_final = laInscripcion["nota_final"]
        return self.repositorioInscripcion.save(inscripcionActual)

    def delete(self, id):
        print("Elimiando inscripcion con id ", id)
        return self.repositorioInscripcion.delete(id)