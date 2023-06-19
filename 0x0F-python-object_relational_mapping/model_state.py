#!/usr/bin/python3
"""Start link class to state table in database """
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer , Column

Base = declarative_base()

class State(Base):
    """ State class child of Base"""
    __table__ = 'states'
    id = Column(Integer,primary_key=True,autoincremnet=True,nullable=False)
    name = Column(String(128), nullable=False)
