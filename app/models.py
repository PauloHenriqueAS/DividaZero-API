"""
models.py

This module contains all models that are being used in api.
"""

from enum import Enum
from typing import Optional, Text
from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    """
    Model of User
    """
    id_user: Optional[int] = None
    email_user: str
    password_user: str
    tipo_user: Optional[int] = None


class Devedor(BaseModel):
    """
    Model of Devedor
    """
    id_devedor: Optional[str] = None
    cpf: str
    nome: Optional[str] = None
    id_endereco: Optional[int] = None
    estado_civil: Optional[str] = None
    nacionalidade: Optional[str] = None

class Endereco(BaseModel):
    """
    Model of Endereco
    """    
    id_endereco: Optional[int] = None
    lograduro: Optional[str] = None
    bairro: Optional[str] = None
    numero: Optional[int] = None
    cep: Optional[str] = None
    complemento: Optional[str] = None


class Credor(BaseModel):
    """
    Model of Credor
    """
    id_credor = Optional[str] = None
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
    status: Optional[str] = None


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


class NacionalidadeEnum(str, Enum):
    """
    Enum with all nationalities in brasilian portuguese 
    """
    ARGENTINO = "Argentino"
    AFEGÃO = "Afegão"
    ALEMÃ = "Alemã"
    AMERICANO = "Americano"
    ANGOLANO = "Angolano"
    ANTIGUANO = "Antiguano"
    ARGÉLIA = "Argélia"
    ARMENO = "Armeno"
    AUSTRALIANO = "Australiano"
    AUSTRÍAC = "Austríac"
    BAHAMENSE = "Bahamense"
    BANGLADESH = "Bangladesh"
    BECHUANO = "Bechuano"
    BELGA = "Belga"
    BELIZENHO = "Belizenho"
    BOLIVIANO = "Boliviano"
    BRASILEIRO = "Brasileiro"
    CAMARONENSE = "Camaronense"
    CANADENSE = "Canadense"
    CHILENO = "Chileno"
    CHINÊS = "Chinês"
    CINGALÊS = "Cingalês"
    COLOMBIANO = "Colombiano"
    COMORENSE = "Comorense"
    COSTARRIQUENHO = "Costarriquenho"
    CROATA = "Croata"
    CUBANO = "Cubano"
    DINAMARQUÊS = "Dinamarquês"
    DOMINICANA = "Dominicana"
    DOMINICANO = "Dominicano"
    EGÍPCIO = "Egípcio"
    EQUATORIANO = "Equatoriano"
    ESCOCÊS = "Escocês"
    ESLOVACO = "Eslovaco"
    ESLOVENO = "Esloveno"
    ESPANHOL = "Espanhol"
    FILIPINA = "Filipina"
    FRANCÊS = "Francês"
    GALÊS = "Galês"
    GANÉS = "Ganés"
    GRANADINO = "Granadino"
    GREGO = "Grego"
    GUATEMALTECO = "Guatemalteco"
    GUIANENSE = "Guianense"
    GUIANÊS = "Guianês"
    HAITIANO = "Haitiano"
    HOLANDÊS = "Holandês"
    HONDURENHO = "Hondurenho"
    HÚNGARO = "Húngaro"
    IEMENITA = "Iemenita"
    INDIANO = "Indiano"
    INDONÉSIO = "Indonésio"
    INGLÊS = "Inglês"
    IRANIANO = "Iraniano"
    IRAQUIANO = "Iraquiano"
    IRLANDÊS = "Irlandês"
    ISRAELITA = "Israelita"
    ITALIANO = "Italiano"
    JAMAICANO = "Jamaicano"
    JAPONÊS = "Japonês"
    LÍBIO = "Líbio"
    MALAIO = "Malaio"
    MARFINENSE = "Marfinense"
    MARROQUINO = "Marroquino"
    MEXICANO = "Mexicano"
    MOÇAMBICANO = "Moçambicano"
    NAMIBIANA = "Namibiana"
    NEOZELANDÊS = "Neozelandês"
    NEPALÊS = "Nepalês"
    NICARAGUENSE = "Nicaraguense"
    NIGERIANO = "Nigeriano"
    NORTE-COREANO = "Norte-coreano"
    NORUEGO = "Noruego"
    OMANENSE = "Omanense"
    PALESTINO = "Palestino"
    PANAMENHO = "Panamenho"
    PAQUISTANÊS = "Paquistanês"
    PARAGUAIO = "Paraguaio"
    PERUANO = "Peruano"
    POLONÊS = "Polonês"
    PORTORRIQUENHO = "Portorriquenho"
    PORTUGUESA = "Portuguesa"
    QATARENSE = "Qatarense"
    QUENIANO = "Queniano"
    ROMENO = "Romeno"
    RUANDÊS = "Ruandês"
    RUSSO = "Russo"
    SALVADORENHO = "Salvadorenho"
    SANTA-LUCENSE = "Santa-lucense"
    SAUDITA = "Saudita"
    SOMALI = "Somali"
    SUECO = "Sueco"
    SUL-AFRICANO = "Sul-Africano"
    SUL-AFRICANO = "Sul-africano"
    SUL-COREANO = "Sul-coreano"
    SURINAMÊS = "Surinamês"
    SUÍÇO = "Suíço"
    SÃO-CRISTOVENSE = "São-cristovense"
    SÃO-VICENTINO = "São-vicentino"
    SÉRVIO = "Sérvio"
    SÍRIO = "Sírio"
    TAILANDÊS = "Tailandês"
    TIMORENSE = "Timorense"
    TRINDADENSE = "Trindadense"
    TURCO = "Turco"
    UCRANIANO = "Ucraniano"
    UGANDENSE = "Ugandense"
    URUGUAIO = "Uruguaio"
    VENEZUELANO = "Venezuelano"
    VIETNAMITA = "Vietnamita"
    ZIMBABUENSE = "Zimbabuense"
    ZIMBABWEANO = "Zimbabweano"
    BARBADENSE = "barbadense"
    ÁRABE = "Árabe"
    OUTRO = "Outro"

class StatusEnum(str, Enum):
    """
    Enum of Divida states
    """
    QUITADA = "Paga"
    ABERTA = "Aberta"
    ATRASADA = "Atrasada"
    RENEGOCIADA = "Renegociada"
