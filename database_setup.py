import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

base = declarative_base()


class User(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    picture = Column(String(250))


class Country(base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Club(base):
    __tablename__ = 'club'
    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(3000), nullable=False)
    Country_id = Column(Integer, ForeignKey('country.id'))
    countryid = relationship("Country", foreign_keys=[Country_id])
    country_name = Column(String(100), ForeignKey('country.name'))
    countryname = relationship("Country", foreign_keys=[country_name])
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return{
            'description': self.description,
            'name': self.name,
            'id': self.id,
            'country_name': self.country_name
        }


engine = create_engine('sqlite:///clubs.db')
base.metadata.create_all(engine)
