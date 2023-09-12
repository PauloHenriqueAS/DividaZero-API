from sqlalchemy import Column, Integer,  String, Text
from app.repositorys.configDb import Base
from app.repositorys.model import UserDb


class Credor(UserDb):
    nome = Column(String, index=True)
    cnpj = Column(String, index=True)
    endereco = Column(Integer,ForeignKey('endereco.id_enderco'))
    