"""
app/Repositorys/debtor_repository.py

This module contains debtor-methods.
"""

from app.models import Credor
from app.repositorys.model import CredorDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

class DebtorRepository:
    """
    Debtor Repository
    """
    def get_debtor_by_cnpj(self, cnpj:str):
        """
        Get data address by cnpj
        """
        try:
            db = SessionLocal()
            credor = db.query(CredorDb).filter(CredorDb.cnpj == cnpj).first()
            db.close()

            if credor is None:
                return {"code": 302, "mensagem": "Usuário não cadastrado"}
            else:
                return {credor}
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}


    def get_debtor_by_id(self, id:str):
        """
        Get data address by id
        """
        try:
            db = SessionLocal()
            credor = db.query(CredorDb).filter(CredorDb.id_credor == id).first()
            db.close()

            if credor is None:
                return {"code": 302, "mensagem": "Usuário não cadastrado"}
            else:
                return {credor}
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}

    def post_debtor(self):
        """
        insert new data debtor
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def update_debtor(self):
        """
        Update new data debtor
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

debtor_repository  = DebtorRepository()
