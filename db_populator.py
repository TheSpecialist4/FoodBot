from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import MainIngredient, Base, Dish

engine = create_engine('sqlite:///foodbot.db')

Base.metadata.bind = engine

DBsession = sessionmaker(bind = engine)

session = DBsession()
obj = session.query(MainIngredient).all()
for a in obj:
    session.delete(a)
    session.commit()

o = session.query(Dish).all()
for x in o:
    session.delete(x)
    session.commit()

# ing1 = MainIngredient(name = "Chicken")
# session.add(ing1)
# session.commit()

# ing2 = MainIngredient(name = "Egg")
# session.add(ing2)
# session.commit()

# ing3 = MainIngredient(name = "Spinach")
# session.add(ing3)
# session.commit()

# dish1 = Dish(name = "Chicken Biryani", main_ingredient = ing1, is_breakfast = 0, description = "Chicken Biryani", 
#             cooking_time = "30 minutes", recipe_link = "www.google.com")
# session.add(dish1)
# session.commit()

# print("added items to db")