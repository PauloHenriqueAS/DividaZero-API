"""
app/Repositorys/term_repository.py

This module contains term-methods.
"""

<<<<<<< Updated upstream
from app.models import TermoDivida
from app.repositorys.model import TermoDividaDb
from .configDb import SessionLocal
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
=======
from sqlalchemy.exc import IntegrityError
from .model import DividaDb, TermoDividaDb
from .configDb import SessionLocal
from sqlalchemy.orm import joinedload
>>>>>>> Stashed changes

class TermRepository:
    """
    Term Repository
    """
    def get_term_by_id(self, id_termo:int):
        """
        Get data term by id
        """
        try:
            db = SessionLocal()
            user = db.query(TermoDividaDb).filter(TermoDividaDb.id_termo == id_termo).first()
            db.close()

            if user is None:
                return {"code": 302, "mensagem": "Termos do usuário não cadastrado"}
            else:
                return { user }
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter termos do usuário. ERRO: {error}"}
        
    def get_all_term_by_id(self, id_user: str):
        """
        Get data term by id
        """
        try:
            db = SessionLocal()
            
            # Faça uma junção entre as tabelas TermoDividaDb e DividaDb usando joinedload
            user_terms = (
                db.query(TermoDividaDb)
                .join(DividaDb, DividaDb.id_divida == TermoDividaDb.id_divida)
                .filter(DividaDb.id_devedor == id_user)
                .all()
            )
            
            db.close()

            if not user_terms:
                return {"code": 302, "mensagem": "Termos do usuário não cadastrado"}
            else:
                # Serialize os resultados, se necessário
                serialized_terms = [term.__dict__ for term in user_terms]
                return {"code": 200, "termos": serialized_terms}
        except IntegrityError as error:
            return {"code": 404, "mensagem": f"Erro ao obter termos do usuário. ERRO: {error}"}

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
