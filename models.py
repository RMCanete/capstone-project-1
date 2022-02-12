"""Model for Capstone1 app."""

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<User #{self.user_id}: {self.username}, {self.email}>"

    @classmethod
    def signup(cls, username, email, user_password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = Bcrypt.generate_password_hash(user_password).decode('UTF-8')

        user = Users(username=username, email=email, user_password=hashed_pwd)

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = Bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False



class Drinks(db.Model):
    
    __tablename__ = 'drinks'

    drink_id = db.Column(db.Integer, primary_key=True)
    drink_ingredients_id = db.Column(db.Text, nullable=False)
    drink_image = db.Column(db.Text, nullable=True)
    drink_instructions = db.Column(db.Text, nullable=True)

class Drink_ingredients(db.Model):
    
    __tablename__ = 'drink_ingredients'

    drink_ingredient_id = db.Column(db.Integer, primary_key=True)
    drink_ingredient_1 = db.Column(db.Text, nullable=True)
    drink_ingredient_2 = db.Column(db.Text, nullable=True)
    drink_ingredient_3 = db.Column(db.Text, nullable=True)
    drink_ingredient_4 = db.Column(db.Text, nullable=True)
    drink_ingredient_5 = db.Column(db.Text, nullable=True)
    quantity_of_ingredient_1 = db.Column(db.Text, nullable=True)
    quantity_of_ingredient_2 = db.Column(db.Text, nullable=True)
    quantity_of_ingredient_3 = db.Column(db.Text, nullable=True)
    quantity_of_ingredient_4 = db.Column(db.Text, nullable=True)
    quantity_of_ingredient_5 = db.Column(db.Text, nullable=True)
    measurement_type_1 = db.Column(db.Text, nullable=True)
    measurement_type_2 = db.Column(db.Text, nullable=True)
    measurement_type_3 = db.Column(db.Text, nullable=True)
    measurement_type_4 = db.Column(db.Text, nullable=True)
    measurement_type_5 = db.Column(db.Text, nullable=True)


class Favorites(db.Model):
    
    __tablename__ = 'favorites'

    favorite_id = db.Column(db.Integer, primary_key=True)
    drink_id = db.Column(db.Integer, db.ForeignKey('drink.drink_id', ondelete="cascade"),
        primary_key=True,)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id', ondelete="cascade"),
        primary_key=True,)
    comment = db.Column(db.Text, nullable=True),
    created_at = db.Column(db.TimeStamp, nullable=False)

def connect_db(app):
    db.app = app
    db.init_app(app)
