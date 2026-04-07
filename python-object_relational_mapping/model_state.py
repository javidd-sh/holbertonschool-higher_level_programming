#!/usr/bin/python3
"""State class definition with SQLAlchemy ORM"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Base class for all tables
Base = declarative_base()


class State(Base):
    """State class mapped to 'states' table"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
