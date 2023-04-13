#####################################MATERIA#############################################
from jc_python_flask.Modelos.Materia import Materia
from jc_python_flask.Repositorios.RepositorioDepartamento import RepositorioDepartamento
from jc_python_flask.Repositorios.RepositorioDepartamento import RepositorioDepartamento
from jc_python_flask.Repositorios.RepositorioMateria import RepositorioMateria


"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMateria():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        print("Creando ControladorMateria")
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        print("Listar todos las materias")
        return self.repositorioMateria.findAll()

    def create(self, laMateria):
        print("Crear una materia")
        nuevaMateria = Materia(laMateria)
        return self.repositorioMateria.save(nuevaMateria)

    def show(self, id):
        print("Mostrando una materia con id ", id)
        laMateria = Materia(self.repositorioMateria.findById(id))
        return laMateria.__dict__

    def update(self, id, laMateria):
        print("Actualizando materia con id ", id)
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = laMateria["nombre"]
        materiaActual.creditos = laMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        print("Eliminando materia con id ", id)
        return self.repositorioMateria.delete(id)

""""
"Relacion departamento y materia

def asignarDepartamento(self, id, id_departamento):
   materiaActual=Materia(self.repositorioMateria.findById(id))
   departamentoActual = 
Departamento(self.repositorioDepartamento.findById(id_departamento))
      materiaActual.departamento=departamentoActual
     return self.repositorioMateria.save(materiaActual)
"""

