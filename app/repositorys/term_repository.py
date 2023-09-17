"""
app/Repositorys/term_repository.py

This module contains term-methods.
"""

from app.models import TermoDivida
from app.repositorys.model import TermoDividaDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError

class TermRepository:
    """
    Term Repository
    """
    def get_term_by_id(self):
        """
        Get data term by id
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def post_term(self, termo:TermoDivida):
        """
        insert new data term
        """
        db_term = TermoDividaDb(**termo.dict())

        db = SessionLocal()
        db.add(db_term)
        db.commit()
        db.refresh(db_term)
        db.close()
        return db_term


    def update_term(self):
        """
        Update data term
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

term_repository = TermRepository()
