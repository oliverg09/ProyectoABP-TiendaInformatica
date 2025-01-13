from pymongo import MongoClient

def get_db():
    # --- BASE DE DATOS LOCAL ---
    # cliente = MongoClient("mongodb://localhost:27017/")
    # --- BASE DE DATOS REMOTA ---
    cliente = MongoClient("mongodb+srv://proyectoabp:proyectoabp1234@cluster0.0slsw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = cliente["gestion"]
    return db