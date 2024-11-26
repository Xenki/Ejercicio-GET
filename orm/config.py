#el enine permiete configurar la conexión a la BD
from sqlalchemy import create_engine
#El session maker permite crear seisones para hacer consultas
#Por cada consulta se abre y cierra una sesión
from sqlalchemy.orm import sessionmaker
#declarative_base permite definir la clase base para mapear las tablas de la BD
from sqlalchemy.ext.declarative import declarative_base

#1.Configurar a la conexiones BD
# servidorBD://usuario:password@url:puerto/nombreBD
URL_BASE_DATOS ="postgresql://usuario-ejemplo:5572@localhost:5432/base-ejemplo"
#Conectarnos al esquema app
engine = create_engine(URL_BASE_DATOS,
                        connect_args={
                            "options": "-csearch_path=app"
                        })

#2. Obtener la clase que nos permite crear objetos tipo session
SessionClass= sessionmaker(engine) 
# Crear una funcion para obteer objetos de la clase SessionClass
def generador_sesion():
    sesion = SessionClass()
    try:
        yield sesion
    finally:
        sesion.close()

#3 Obtenerr la clase base para mapear tablas
BaseClass = declarative_base()