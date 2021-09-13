from src import app, db, bcrypt
from src.models import User, Scores#, Levels
from sqlalchemy import desc, func
from sqlalchemy import select
#user = db.session.query(User)
#user1 = User.query.all()
#for user in user:
 #   print(user.username)
#print(user1)


#score = db.session.query(Scores, Levels).join(Levels, Levels.id==Scores.id)
#for scoes in score.all():
 #   for a in scoes:
  #      print(level)
#for c, i in db.session.query(func.max(Levels.level_score), Scores, Levels).filter(Scores.id == Levels.id).where(Scores.level==1).order_by(func.max(Scores.level)):
  # print ("ID: {} Name: {} Level: {} Score: {}".format(c.id,c.level, i.id, i.level_score))


#for c, i in db.session.query(Scores, Levels).filter(Scores.id == Levels.id).group_by(Scores.level):#.where(Levels.level_score)
   #print ("ID: {} Name: {} Level: {} Score: {}".format(c.id,c.level, i.id, i.level_score))


#for c in db.session.query(Scores.level_score):
 #   print(c.level_score).func.max()
#print(select(Scores.level, func(max(Levels.level_score))).select_from(Scores, Levels).filter(Levels.id == Scores.id).group_by(Scores.level))

#for c, i in db.session.query(Scores, Levels).filter(Scores.id == Levels.id).where(func(max(Levels.level_score))):
   #print ("ID: {} Name: {} Level: {} Score: {}".format(c.id,c.level, i.id, i.level_score))

#a =db.session.query(func.max(Levels.level_score)).scalar()
#for b in db.session.query(Scores.level,func.max(Levels.level_score)).filter(Scores.id == Levels.id).group_by(Scores.level).order_by(Scores.level).all():
#print(a)
  #  print(b)

c = db.session.query(User.username,func.max(Scores.level_score)).filter(Scores.user_id == User.id)\
        .where(Scores.level==2).group_by(User.username).order_by(User.username).all()
#print(a)
print(c)


#level = Scores.query.get(Scores.level)
#print(level)