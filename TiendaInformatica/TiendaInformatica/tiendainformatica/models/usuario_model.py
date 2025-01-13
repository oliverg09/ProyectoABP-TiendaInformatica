from pydantic import BaseModel

class UserModel(BaseModel):
    nombre: str
    contraseña: str