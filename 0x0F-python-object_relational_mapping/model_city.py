#!/usr/bin/python3
"""Start link class to cities table in database """
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer , Column, ForeignKey

Base = declarative_base()

class City(Base):
    """ City class child of Base"""
    __table__ = 'cities'
    id = Column(Integer,primary_key=True,autoincremnet=True,nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
