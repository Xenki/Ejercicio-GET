import orm.modelos as modelos
from sqlalchemy.orm import Session

# Esta función es llama por api.py para atender GET '/usuarios/{id}'
#select * from app.usuarios where id = id_usuario
def usuario_por_id(sesion: Session,id_usuario:int):
    print("select * from aoo.usuarios where id = ",id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id == id_usuario).first()

def fotos_por_id(sesion: Session,id_foto:int):
    print("select * from aoo.fotos where id = ",id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Usuario.id == id_foto).first()

def compras_por_id(sesion: Session,id_compra:int):
    print("select * from aoo.compras where id = ",id_compra)
    return sesion.query(modelos.Compra).filter(modelos.Usuario.id == id_compra).first()
