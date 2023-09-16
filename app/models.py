"""
models.py

This module contains all models that are being used in api.
"""

from typing import Optional, Text
from pydantic import BaseModel
from datetime import date
from .enums import NacionalidadeEnum, StatusEnum, EstadoCivil

class User(BaseModel):
    """
    Model of User
    """
    id_user: Optional[int] = None
    email_user: str
    password_user: str
    tipo_user: Optional[str] = None

class Devedor(BaseModel):
    """
    Model of Devedor
    """
    id_devedor: Optional[str] = None
    id_user: Optional[str] = None
    cpf: str
    nome: Optional[str] = None
    id_endereco: Optional[int] = None
    estado_civil: Optional[EstadoCivil] = None
    nacionalidade: Optional[NacionalidadeEnum] = None

class Endereco(BaseModel):
    """
    Model of Endereco
    """    
    id_endereco: Optional[int] = None
    logradouro: Optional[str] = None
    bairro: Optional[str] = None
    numero: Optional[int] = None
    cep: Optional[str] = None
    complemento: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None

class Credor(BaseModel):
    """
    Model of Credor
    """
    id_credor: Optional[str] = None
    id_user: Optional[str] = None
    nome: Optional[str] = None
    cnpj: Optional[str] = None
    id_endereco: Optional[int] = None

class Divida(BaseModel):
    """
    Model of Divida
    """
    id_divida: Optional[int] = None
    id_credor: Optional[str] = None
    id_devedor: Optional[str] = None
    num_contrato: Optional[str] = None
    termo_divida: Optional[Text] = None
    data_divida: Optional[date] = None
    montante_valor:  Optional[float] = None
    montante_atrasado: Optional[float] = None
    status: Optional[StatusEnum] = None
    produto: Optional[str] = None

class TermoDivida(BaseModel):
    """
    Model of termo divida
    """
    id_termo: Optional[int] = None
    id_divida: Optional[int] = None
    num_parcela: Optional[int] = None
    termo_renegociacao: Optional[Text] = None
    data_renegociacao: Optional[date] = None
    assinatura_devedor: Optional[str] = None
    assinatura_credor: Optional[str] = None

class Parcela(BaseModel):
    """
    Model of Parcela
    """
    id_parcela: Optional[int] = None
    id_termo: Optional[int] = None
    valor_parcela: Optional[float] = None
    data_vencimento: Optional[date] = None
    parcela_paga: Optional[bool] = None

class Parcelamento(BaseModel):
    valor: float
    qtd: int
