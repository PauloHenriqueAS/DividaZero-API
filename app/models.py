"""
models.py

This module contains all models that are being used in api.
"""

from typing import Optional, Text
from pydantic import BaseModel

class User(BaseModel):
    """
    Model of User
    """
    id_user: Optional[int] = None
    email_user: str
    password_user: str
