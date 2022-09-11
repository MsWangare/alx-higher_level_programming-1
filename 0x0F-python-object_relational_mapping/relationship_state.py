#!/usr/bin/python3
"""State model ORM"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
            nullable=False, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan", backref=backref("state", cascade="all"), single_parent=True)
