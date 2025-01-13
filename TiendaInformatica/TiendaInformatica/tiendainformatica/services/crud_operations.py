from services.mongo_service import get_db
from services.query_operations import calcularId

def crearUsuario(user_data):
    db = get_db()
    coleccion = db["usuarios"]
    coleccion.insert_one(user_data)

def insertarProducto(producto):
    db = get_db()
    coleccion = db["productos"]
    coleccion.insert_one(producto)

def cargarImagen():
    pass


def comprarProducto(order_data):
    compra = False
    db = get_db()
    pedidos = db["pedidos"]
    if modificarProducto({"nombre":order_data['nombre_producto'],'stock':{"$gt":0}},{'$inc':{'stock':-order_data['stock']}}):
        pedidos.insert_one(order_data)
        producto = db['productos'].find_one({"nombre":order_data['nombre_producto']})
        if producto['stock'] <= 0:
            eliminarProducto({"nombre":order_data['nombre_producto']})
        compra = True
    return compra



def modificarProducto(product_filter:dict,product_data:dict):
    modificado = False
    db = get_db()
    coleccion = db["productos"]
    #(product_filter={"nombre":'producto'},product_data={'$set':{"categoria":'coches',...}})
    data = coleccion.update_one(product_filter,product_data)
    if data.modified_count > 0:
        modificado = True
    return modificado

def eliminarProducto(product_filter:dict):
    db = get_db()
    coleccion = db["productos"]
    data = coleccion.delete_one(product_filter)