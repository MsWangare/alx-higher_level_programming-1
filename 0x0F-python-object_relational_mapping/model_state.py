#!/usr/bin/python3
"""State model ORM"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
