#!/usr/bin/env python3
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

"""File name: database_setup.py

That's Database Setup file:
    1. run this file to setup your database
    2. run after this lotsofcar.py    

More details can be found in the README.md file,
which is included with this project.
"""


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)    
    email = Column(String(100), nullable=False)
    image = Column(String(100))
    password = Column(String(100))
    job = Column(String(100))
    salaty = Column(String(100)) 
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'image': self.code,
            'job': self.job,
            'storage': self.salaty
        }

    

class newUrls(Base):
    __tablename__ = 'newurls'

    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)    
    code = Column(String(90000), nullable=False)
    url = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'code': self.code,
            'url': self.url            
        }


class Skills(Base):
    __tablename__ = 'skills'

    id = Column(Integer, primary_key=True)
    name = Column(String(350), nullable=False)    
    skill = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'code': self.skill,        
        }




    




engine = create_engine('sqlite:///mpasta.db')
Base.metadata.create_all(engine)
