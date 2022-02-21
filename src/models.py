import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

tabla_pivote1 = Table('personaje_favorito', Base.metadata,
    Column('usuario_id', ForeignKey('usuario.id'), primary_key=True),
    Column('personaje_id', ForeignKey('personaje.id'), primary_key=True))

tabla_pivote2 = Table('planeta_favorito', Base.metadata,
    Column('usuario_id', ForeignKey('usuario.id')),
    Column('planeta_id' , ForeignKey('planeta.id')))

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    contrasena = Column(String(100), nullable=False)
    # personaje_id = Column(Integer, ForeignKey('personaje.id'))
    personaje = relationship('Personaje', secondary=tabla_pivote1)
    # planeta_id = Column(Integer, ForeignKey('planeta.id'))
    planeta = relationship('Planeta' , secondary=tabla_pivote2)

class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(100), nullable=True)
    eye_color = Column(String(100), nullable=True)
   

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_planeta = Column(String(250), nullable=False)
    gravity = Column(String(100), nullable=True)
    climate = Column(String(100), nullable=True)
   
  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')