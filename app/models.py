"""
models.py

This module contains all models that are being used in api.
"""

from enum import Enum
from typing import Optional, Text
from pydantic import BaseModel

class User(BaseModel):
    """
    Model of User
    """
    id_user: Optional[int] = None
    email_user: str
    password_user: str

## TODO FAZER as models nesse jeito, **lembrar que todo paramtro que não necessariamente venha na requisição na controller deve ser nulo**
class Devedor(BaseModel):
    """
    Model of Devedor
    """
    id_devedor: Optional[int] = None
    cpf: str
    nome: Optional[str] = None
    id_endereco: Optional[int] = None
    estado_civil: Optional[str] = None
    nacionalidade: Optional[str] = None

## TODO FAZER UNS ENUM ASSIM
 #   nacionalidade = Column(Enum('Argentino', 'Afegão', 'Alemã', 'Americano', 'Angolano', 'Antiguano', 'Argélia', 'Armeno', 'Australiano', 'Austríac', 'Bahamense', 'Bangladesh', 'Bechuano', 'Belga', 'Belizenho', 'Boliviano', 'Brasileiro', 'Camaronense', 'Canadense', 'Chileno', 'Chinês', 'Cingalês', 'Colombiano', 'Comorense', 'Costarriquenho', 'Croata', 'Cubano', 'Dinamarquês', 'Dominicana', 'Dominicano', 'Egípcio', 'Equatoriano', 'Escocês', 'Eslovaco', 'Esloveno', 'Espanhol', 'Filipina', 'Francês', 'Galês', 'Ganés', 'Granadino', 'Grego', 'Guatemalteco', 'Guianense', 'Guianês', 'Haitiano', 'Holandês', 'Hondurenho', 'Húngaro', 'Iemenita', 'Indiano', 'Indonésio', 'Inglês', 'Iraniano', 'Iraquiano', 'Irlandês', 'Israelita', 'Italiano', 'Jamaicano', 'Japonês', 'Líbio', 'Malaio', 'Marfinense', 'Marroquino', 'Mexicano', 'Moçambicano', 'Namibiana', 'Neozelandês', 'Nepalês', 'Nicaraguense', 'Nigeriano', 'Norte-coreano', 'Noruego', 'Omanense', 'Palestino', 'Panamenho', 'Paquistanês', 'Paraguaio', 'Peruano', 'Polonês', 'Portorriquenho', 'Portuguesa', 'Qatarense', 'Queniano', 'Romeno', 'Ruandês', 'Russo', 'Salvadorenho', 'Santa-lucense', 'Saudita', 'Somali', 'Sueco', 'Sul-Africano', 'Sul-africano', 'Sul-coreano', 'Surinamês', 'Suíço', 'São-cristovense', 'São-vicentino', 'Sérvio', 'Sírio', 'Tailandês', 'Timorense', 'Trindadense', 'Turco', 'Ucraniano', 'Ugandense', 'Uruguaio', 'Venezuelano', 'Vietnamita', 'Zimbabuense', 'Zimbabweano', 'barbadense', 'Árabe'), nullable=True, index=True)
class NacionalidadeEnum(str, Enum):
    BRASILEIRO = "Brasileiro"
    ESTRANGEIRO = "Estrangeiro"
    OUTRO = "Outro"
