import hashlib
import os

def generarHash(password:str) -> tuple:
    """Funcion que recibe una contraseña
    en string y devuelve un hash de esa contraseña
    en hexadecimal con el algoritmo sha256 y su sal"""
    iteraciones = 500000
    password = password.encode('utf-8')
    # Es recomendable usar una herramienta para generar las sales
    # y las sales deben ser al menos de 16 bytes
    sal = os.urandom(16)
    #Elegimos el algoritmo de encriptamiento sha256
    # La sal sera unica para cada contraseña
    key = hashlib.pbkdf2_hmac("sha256",password,sal,iteraciones)
    return (key.hex(),sal)

def validarPassword(passwordValidar:str,sal,passwordUser:str) -> bool:
    """Funcion que recibe una sal de encriptacion en string,
    la contraseña que quieres validar y un hash
    de un usuario que ya esta registrado para
    comprobar si son iguales."""
    iteraciones = 500000
    passwordValidar = passwordValidar.encode("utf-8")
    #La sal es la de un usuario que ya esta registrado
    key = hashlib.pbkdf2_hmac("sha256",passwordValidar,sal,iteraciones)
    return key.hex() == passwordUser