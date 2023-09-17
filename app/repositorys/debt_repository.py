"""
app/Repositorys/debt_repository.py

This module contains debt-methods.
"""

from app.models import Divida
from app.repositorys.model import DividaDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

class DebtRepository:
    """
    Debt Repository
    """
    def get_debt_by_id(self, id:int):
        """
        Get data debt by id
        """
        try:
            db = SessionLocal()
            divida = db.query(DividaDb).filter(DividaDb.id_divida == id).first()
            db.close()

            if divida is None:
                return {"code": 302, "mensagem": "Usuário não cadastrado"}
            else:
                return {divida}
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}

    def get_all_debt_by_user(self, id_devedor:str):
        """
        Get all data debt by id devedor
        """
        try:
            db = SessionLocal()
            dividas = db.query(DividaDb).filter(DividaDb.id_devedor == id_devedor).all()
            db.close()

            if not dividas:
                return {"code": 302, "mensagem": "Usuário não cadastrado ou sem dívidas"}
            else:
                return {"code": 200, "dívidas": [debt.__dict__ for debt in dividas]}
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter usuário. ERRO: {error}"}

    def post_debt(self):
        """
        insert new data debt
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def update_debt(self):
        """
        Update new data debt
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

debt_repository  = DebtRepository()
