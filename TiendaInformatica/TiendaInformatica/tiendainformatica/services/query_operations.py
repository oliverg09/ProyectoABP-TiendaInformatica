from pymongo import MongoClient
from services.mongo_service import get_db

def consultaUsuario(user_data):
    db = get_db()
    coleccion = db["usuarios"]
    data = coleccion.find_one(user_data)
    return data

def consultarProducto(product_data):
    db = get_db()
    coleccion = db["productos"]
    data = coleccion.find_one(product_data)
    return data

def consultarProductos():
    db = get_db()
    coleccion = db["productos"]
    data = coleccion.find()
    return list(data)

def consultarCategoriasFiltros():
    db = get_db()
    coleccion = db["productos"]
    categorias_distintas = coleccion.distinct('categoria')
    return categorias_distintas

def consultarMarcasFiltros():
    db = get_db()
    coleccion = db["productos"]
    marcas_distintas = coleccion.distinct('marca')
    return marcas_distintas

def consultarTipoUsuario(user_data):
    usuario = consultaUsuario(user_data)
    if usuario == None:
        return None
    else:
        return usuario["usuario"]



def eliminarProducto(product_data:dict):
    db = get_db()
    coleccion = db["productos"]
    #product_data={"nombre":'producto'}
    data = coleccion.delete_one(product_data)


def consultarPedidosCliente(nombreCliente):
    db = get_db()
    coleccion = db["pedidos"]
    data = coleccion.find({"usuario_cliente":nombreCliente})
    return data

def calcularId():
    db = get_db()
    coleccion = db["pedidos"]
    consulta = coleccion.aggregate([ 
        {
            "$group":{
                "_id":None,
                "id_maximo":{"$max":"$id_pedido"}
            }
        }
    ])
    for pedido in consulta:
        if pedido['id_maximo'] != None:
            return pedido['id_maximo'] + 1
        else:
            return 1
    

def consultaPrueba():
    db = get_db()
    coleccion = db["productos"]
    consulta = coleccion.find({"precio":{"$gt":1000}},{"nombre":1,"precio":1})
    # productos = consultarProductos()
    # consulta = productos.limit(10)
    # consulta2 = {'$gt':100}
    return consulta

def consultarProductosFiltros(nombre,categoria,marca,precio_min,precio_max,stock_min,stock_max):
    Almacen_Consultas = []
    db = get_db()
    coleccion = db["productos"]
    consultarNombre(nombre,Almacen_Consultas)
    consultarMarcas(marca,Almacen_Consultas)
    consultarCategorias(categoria,Almacen_Consultas)
    consultaPrecio(precio_min, precio_max,Almacen_Consultas)
    consultarStock(stock_min, stock_max,Almacen_Consultas)
    consulta = coleccion.aggregate(Almacen_Consultas)
    return list(consulta)

    
def consultarNombre(nombre, Almacen_Consultas:list):
    if nombre != "":     
        Almacen_Consultas.append({"$match":{"nombre":nombre}})
    
def consultarCategorias(categoria,Almacen_Consultas:list): 
    if categoria != None:  
        print(categoria)
        Almacen_Consultas.append({"$match":{"categoria":categoria}})


def consultarMarcas(marca,Almacen_Consultas:list):
    if marca != None:
        Almacen_Consultas.append({"$match":{"marca":marca}})
    

    
def consultaPrecio(precio_min, precio_max, Almacen_Consultas:list):  # Funcion para los precios 

    if precio_min.isdigit() and precio_max.isdigit():  #Pregunto si se pueden convertir en entero por lo cual valido si esta vacio o introdujo letras
        Almacen_Consultas.append({"$match":{"precio": {"$gte": int(precio_min),"$lte": int(precio_max)}}})

    elif precio_min.isdigit():
        Almacen_Consultas.append({"$match":{"precio": {"$gte": int(precio_min)}}})

    elif precio_max.isdigit():
        Almacen_Consultas.append({"$match":{"precio": {"$lte": int(precio_max)}}})

    else:
        print("No entro Precio")



def consultarStock(stock_min, stock_max, Almacen_Consultas:list): # Es Igual que el stock

    if stock_min.isdigit() and stock_max.isdigit():
        Almacen_Consultas.append({"$match":{"stock": {"$gte": int(stock_min),"$lte": int(stock_max)}}})

                

    elif stock_min.isdigit():
        Almacen_Consultas.append({"$match":{"stock": {"$gte": int(stock_min)}}})
        print("Entro en MIN")
   
        
    elif stock_max.isdigit():
        Almacen_Consultas.append({"$match":{"stock": {"$lte": int(stock_max)}}})

    else:
        print("No entro Stock")
    
# ---------------- CONSULTAS GENERALES ----------------

def consultaProductoMasVendido():
    """Consulta la cual nos conseguirá el producto más vendido"""

    db = get_db()
    coleccion = db["pedidos"]
    vendidos = coleccion.aggregate([
        {"$group": {"_id": "$nombre_producto", "totalVendido": {"$sum": "$stock"}}},
        {"$sort": {"totalVendido": -1}},  # Ordenamos de mayor a menor
    ])

    resultado = [] # Se guardaran los resultados de la consulta

    try:
        productoMasVendido = next(vendidos)  # Conseguir el primer valor (producto más vendido)
        cantidadMaxima = productoMasVendido["totalVendido"]
        resultado.append({
            "nombre": productoMasVendido["_id"],
            "cantidad": productoMasVendido["totalVendido"]
        })

        for producto in vendidos: # Comprobar si hay mas productos con la misma cantidad
            if producto["totalVendido"] == cantidadMaxima:
                resultado.append({
                    "nombre": producto["_id"],
                    "cantidad": producto["totalVendido"]
                })
        return resultado
    
    except StopIteration:  
        resultado = None
        return resultado
    
def consultaProductoMasVendidoPorCategoria():
    """Consulta la cual nos conseguirá el producto más vendido por categoría"""

    db = get_db()  
    coleccion = db["productos"]
    coleccion2 = db["pedidos"] 
    categorias = consultarCategoriasFiltros() 

    resultado = []
    
    for categoria in categorias:
        productos = coleccion.find({"categoria": categoria})

        nombres_productos = []  

        for producto in productos:
            nombre_producto = producto["nombre"]
            nombres_productos.append(nombre_producto)

        vendidos = coleccion2.aggregate([
            {"$match": {"nombre_producto": {"$in": nombres_productos}}},  
            {"$group": {"categoria": {"$first": categoria}, "_id": "$nombre_producto", "totalVendido": {"$sum": "$stock"}}},
            {"$sort": {"totalVendido": -1}},  
        ])

        try:
            productoMasVendidoCategoria = next(vendidos) 
            cantidadMaxima = productoMasVendidoCategoria["totalVendido"]
            resultado.append({
                "categoria": productoMasVendidoCategoria["categoria"],
                "nombre": productoMasVendidoCategoria["_id"],
                "cantidad": productoMasVendidoCategoria["totalVendido"]
            })

            for producto in vendidos: 
                if producto["totalVendido"] == cantidadMaxima:
                    resultado.append({
                    "categoria": producto["categoria"],
                    "nombre": producto["_id"],
                    "cantidad": producto["totalVendido"]
                })
    
        except StopIteration:  
            return None
    return resultado

def consultaProductoMasVendidoPorMarca():
    """Consulta la cual nos conseguirá el producto más vendido por marca"""

    db = get_db()  
    coleccion = db["productos"]
    coleccion2 = db["pedidos"] 
    marcas = consultarMarcasFiltros() 

    resultado = []
    
    for marca in marcas:
        productos = coleccion.find({"marca": marca})

        nombres_productos = []

        for producto in productos:
            nombre_producto = producto["nombre"]    
            nombres_productos.append(nombre_producto)
        
        vendidos = coleccion2.aggregate([
            {"$match": {"nombre_producto": {"$in": nombres_productos}}},  
            {"$group":  {"marca": {"$first": marca},"_id": "$nombre_producto", "totalVendido": {"$sum": "$stock"}}},
            {"$sort": {"totalVendido": -1}},  
        ])

        try:
            productoMasVendidoMarca = next(vendidos) 
            cantidadMaxima = productoMasVendidoMarca["totalVendido"]
            resultado.append({
                "marca": productoMasVendidoMarca["marca"],
                "nombre": productoMasVendidoMarca["_id"],
                "cantidad": productoMasVendidoMarca["totalVendido"]
            }) 

            for producto in vendidos: 
                if producto["totalVendido"] == cantidadMaxima:
                    resultado.append({
                    "marca": producto["marca"],
                    "nombre": producto["_id"],
                    "cantidad": producto["totalVendido"]
                }) 
    
        except StopIteration:  
            return None
    return resultado

def consultaCantidadVendidaProducto():
    """Consulta la cual nos conseguirá la cantidad vendida de cada producto"""

    db = get_db()
    coleccion = db["pedidos"]
    vendidos = coleccion.aggregate([
        {"$group": {"_id": "$nombre_producto", "totalVendido": {"$sum": "$stock"}}},
        {"$sort": {"totalVendido": -1}}, 
    ])

    resultado = []

    try:
        for productoVendido in vendidos:
            resultado.append({
                "nombre": productoVendido["_id"],
                "cantidad": productoVendido["totalVendido"]
            }) 
        if resultado is None:  # Si no se encontraron productos
            resultado = None
        return resultado

    except StopIteration:  
        resultado = None
        return resultado

def consultaDineroRecaudado():
    """Consulta la cual nos conseguirá la recaudación de ventas total"""

    db = get_db()
    coleccion = db["pedidos"]
    recaudado = coleccion.aggregate([
        {"$group": {"_id": None, "totalRecaudado": {"$sum": "$precio"}}}
    ])

    resultado = []
    
    try:
        dineroRecaudado = next(recaudado)
        resultado.append({
                "cantidad": dineroRecaudado["totalRecaudado"]
            }) 
        return resultado

    except StopIteration:  
        resultado = None
        return resultado

# --------------------------------
