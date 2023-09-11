"""
app/Repositorys/model.py

This module contains database models.
"""

from sqlalchemy import Column, Integer, String, Text
from app.repositorys.configDb import Base

class UserDb(Base):
    '''
    Model User Database
    '''
    __tablename__ = 'tb_usuario'
    __table_args__ = {"schema": "saim"}

    id_user = Column(Integer, primary_key=True, index=True)
    email_user = Column(String, index=True)
    password_user = Column(String, index=True)
