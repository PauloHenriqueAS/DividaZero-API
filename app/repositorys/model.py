"""
app/Repositorys/model.py

This module contains database models.
"""

from sqlalchemy import Boolean, Column, Date, Double, ForeignKey, Integer, String, Text
#from app.db.database import Base
from app.repositorys.configDb import Base


class UserDb(Base):
    '''
    Model User Database
    '''
    __tablename__ = 'tb_usuario'
    __table_args__ = {"schema": "divida_zero"}

    id_user = Column(Integer, primary_key=True, index=True)
    email_user = Column(String, index=True, nullable=False)
    password_user = Column(String, index=True, nullable=False)
    tipo_user = Column(String, index=True, nullable=False)


class EnderecoDb(Base):
    """
    Model Endereço Database
    """
    __tablename__ = 'tb_endereco'
    __table_args__ = {"schema": "divida_zero"}

    id_endereco = Column(Integer, primary_key=True, index=True)
    logradouro = Column(String, nullable=False, index=True)
    bairro = Column(String, nullable=False, index=True)
    numero = Column(Integer, index=True)
    cep = Column(String, nullable=False, index=True)
    complemento = Column(String, index=True)
    cidade = Column(String, nullable=False, index=True)
    estado = Column(String, nullable=False, index=True)


class DevedorDB(Base):
    """
    Model Devedor Database
    """
    __tablename__ = 'tb_devedor'
    __table_args__ = {"schema": "divida_zero"}

    id_devedor = Column(String, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('UserDb.id_user'), index=True, nullable=True)
    cpf = Column(String, index=True, nullable=False)
    nome = Column(String, index=True, nullable=True)
    id_endereco = Column(Integer, ForeignKey('EnderecoDb.id_endereco'), index=True, nullable=True)
    estado_civil = Column(String, index=True, nullable=True)
    nacionalidade = Column(String, index=True, nullable=True)


class CredorDb(Base):
    """
    Model Credor Database
    """
    __tablename__ = 'tb_credor'
    __table_args__ = {"schema": "divida_zero"}

    id_credor = Column(String, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('UserDb.id_user'), index=True, nullable=True)
    nome = Column(String, index=True)
    cnpj = Column(String, index=True)
    id_endereco = Column(Integer, ForeignKey('EnderecoDb.id_endereco'), index=True)


class DividaDb(Base):
    """
    Model Divida Database
    """
    __tablename__ = 'tb_divida'
    __table_args__ = {"schema": "divida_zero"}

    id_divida = Column(Integer, primary_key=True, index=True)
    id_credor = Column(Integer, ForeignKey("CredorDb.id_credor"), nullable=False, index=True)
    id_devedor = Column(Integer, ForeignKey("DevedorDb.id_devedor"), nullable=False, index=True)
    num_contrato = Column(String, nullable=False, index=True)
    termo_divida = Column(Text, nullable=False, index=True)
    data_divida = Column(Date, nullable=False, index=True)
    montante_valor = Column(Double, nullable=False, index=True)
    montante_atrasado = Column(Double, nullable=False, index=True)
    status = Column(String, nullable=False, index=True)
    produto = Column(String, nullable=False, index=True)


class TermoDividaDb(Base):
    """
    Model Termo de confição de divida Database
    """
    __tablename__ = 'tb_termo_conf_divida'
    __table_args__ = {"schema": "divida_zero"}

    id_termo = Column(Integer, primary_key=True, index=True)
    id_divida = Column(Integer, nullable=False, index=True)
    num_parcela = Column(Integer, index=True)
    termo_renegociacao = Column(Text, index=True)
    data_renegociacao = Column(Date, index=True)
    assinatura_devedor = Column(String, index=True, nullable=True)
    assinatura_credor = Column(String, index=True, nullable=True)


class ParcelaDb(Base):
    """
    Model Parcela de renegociação de divida Database
    """
    __tablename__ = 'tb_parcela'
    __table_args__ = {"schema": "divida_zero"}

    id_parcela = Column(Integer, primary_key=True, index=True)
    id_termo = Column(Integer, nullable=False, index=True)
    valor_parcela = Column(Double, index=True)
    data_vencimento = Column(Date, index=True)
    parcela_paga = Column(Boolean, index=True, nullable=True)
