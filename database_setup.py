import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///foodbot.db')
Base.metadata.create_all(engine)

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
    is_breakfast = Column(Integer, nullable = False)
    description = Column(String(250))
    cooking_time = Column(String(30))
    recipe_link = Column(String(100), nullable = False)
    main_ingredient_id = Column(Integer, ForeignKey('main_ingredient.id'))
    main_ingredient = relationship(MainIngredient)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'isBreakfast': self.isBreakfast,
            'description': self.description,
            'cookingTime': self.cookingTime
        }