"""
app/Repositorys/lender_repository.py

This module contains lender-methods.
"""

from app.models import Devedor
from app.repositorys.model import DevedorDB
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

class LenderRepository:
    """
    Lender Repository
    """
    def get_lerder_by_cpf(self,cpf:str):
        """
        Get data lender by cpf
        """
        try:
            db = SessionLocal()
            devedor = db.query(DevedorDB).filter(DevedorDB.cpf == cpf).first
            db.close()
            if devedor is None:
                return {"code": 302, "mensagem": "Usuário não cadastrado"}
            else:
                return {devedor}
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}

    def get_lerder_by_id(self, id:str):
        """
        Get data lender by id
        """
        try:
            db = SessionLocal()
            devedor = db.query(DevedorDB).filter(DevedorDB.id_devedor == id).first
            db.close()

            if devedor is None:
                return {"code": 302, "mensagem": "Usuário não cadastrado"}
            else:
                return {devedor}
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}


    def post_lender(self):
        """
        insert new data lender
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def update_lender(self):
        """
        Update data lender
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

lender_repository  = LenderRepository()
