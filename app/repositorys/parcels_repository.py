"""
app/Repositorys/parcels_repository.py

This module contains parcels-methods.
"""

from app.models import Parcela
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from .model import ParcelaDb
from .configDb import SessionLocal

class ParcelsRepository:
    """
    Parcels Repository
    """
    def get_parcels_by_id(self):
        """
        Get data parcel by id
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}
    
    def get_parcels_by_term(self):
        """
        Get data parcel by term
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def post_parcels(self, parcela:Parcela):
        """
        insert new data parcel
        """
        db_parcela = ParcelaDb(**parcela.dict())

        db = SessionLocal()
        db.add(db_parcela)
        db.commit()
        db.refresh(db_parcela)
        db.close()

        return db_parcela

    def update_parcels(self):
        """
        Update data parcel
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def generate_id_parcela(self):
        """
        Generate new id user to insert method
        """
        try:
            db = SessionLocal()
            max_id_parcela = db.query(func.max(ParcelaDb.id_parcela)).scalar()
            db.close()
            if max_id_parcela is not None:
                return max_id_parcela + 1
        except Exception as error:
            return {"code": 404, "mensagem": f"Erro ao consultar id máximo. ERRO: {error}"}

parcels_repository = ParcelsRepository()
