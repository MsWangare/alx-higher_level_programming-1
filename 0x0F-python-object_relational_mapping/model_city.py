#!/usr/bin/python3
"""City model ORM"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
            nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)
