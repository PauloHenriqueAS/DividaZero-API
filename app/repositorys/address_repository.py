
"""
app/Repositorys/address_repository.py

This module contains address-methods.
"""

from app.models import Endereco
from app.repositorys.model import EnderecoDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

class AddressRepository:
    """
    Address Repository
    """
    def get_address_by_id(self, id:int):
        """
        Get data address by id
        """
        try:
            db = SessionLocal()
            endereco = db.query(EnderecoDb).filter(EnderecoDb.id_endereco == id).first()
            db.close()

            if endereco is None:
                return {"code": 302, "mensagem": "Endereço não cadastrado"}
            else:
                return { endereco }
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}

        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def post_address(self):
        """
        insert new data address
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def update_address(self):
        """
        Update new data address
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

address_repository  = AddressRepository()
