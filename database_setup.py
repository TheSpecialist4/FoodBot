import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class MainIngredient(Base):
    __tablename__ = "main_ingredient"
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

class Dish(Base):
    __tablename__ = "dish"
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    isBreakfast = Column(Integer, nullable = False)
    description = Column(String(250))
    cookingTime = Column(String(30))

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'isBreakfast': self.isBreakfast,
            'description': self.description,
            'cookingTime': self.cookingTime
        }

engine = create_engine('sqlite:///foodbot.db')

Base.metadata.create_all(engine)