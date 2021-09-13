from src import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    #__tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    score = db.relationship('Scores', backref='useru', lazy=True)#, cascade="all, delete-orphan"

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Scores(db.Model):
    #__tablename__ = "scores"
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, nullable=False)
    level_score = db.Column(db.Integer, nullable=False)
    #
    #title = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #users = db.relationship('Levels', backref='scoresu', lazy=True)#'dynamic'
    #level_id = db.Column(db.Integer, db.ForeignKey('levels.id'), nullable=False)
    #user_ida = db.relationship("User", back_populates="score")

    def __repr__(self):
        return f"Score('{self.level}','{self.level_score}')"

#class Levels(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  level_score = db.Column(db.Integer)
   # scores = db.Column(db.Integer, db.ForeignKey('scores.id'), nullable=False)

    #def __repr__(self):
     #   return f"Sc()"