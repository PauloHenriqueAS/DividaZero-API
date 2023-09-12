from sqlalchemy import Column, Integer, String, Text
from app.repositorys.configDb import Base


class enderecoDb(Base):
    __tablename__ = 'endereco'
    __table_args__ = {"schema": "saim"}

    id_endereco = Column(Integer,primary_key=True, index=True)
    lograduro = Column(String,nullable=False)
    bairro = Column(String,nullable=False)
    numero = Column(Integer)
    cep = Column(String,nullable=False)
    complemento = Column(String)
