from app import db

class MainIngredient(db.Model):
    __tablename__ = "main_ingredient"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

class Dish(db.Model):
    __tablename__ = "dish"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)
    is_breakfast = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(250))
    cooking_time = db.Column(db.String(30))
    recipe_link = db.Column(db.String(100), nullable = False)
    main_ingredient_id = db.Column(db.Integer, db.ForeignKey('main_ingredient.id'))
    main_ingredient = db.relationship(MainIngredient)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'isBreakfast': self.isBreakfast,
            'description': self.description,
            'cookingTime': self.cookingTime
        }