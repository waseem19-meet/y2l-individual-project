from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_offer(subject, content, user_id, user_Num):
    print("Added an offer!")
    offer = Offer(subject=subject, content=content, user_id=user_id, user_Num=user_Num)
    session.add(offer)
    session.commit()


def get_all_offers():
  offers = session.query(Offer).all()
  return offers

# def delete_offer():
# 	offer = session.query(Offer).filter_by(id=id).first()
# 	session.delete(offer)
# 	session.commit()

def get_phone_num_from_id(user_id):
  user = session.query(User).filter_by(id=user_id).first()
  num = user.PhoneNum
  return num


def add_user(status, name, email, password, PhoneNum):
    print("Added a user!")
    user = User(status=status, name=name, email=email, password=password, PhoneNum=PhoneNum)
    session.add(user)
    session.commit()



def get_all_users():
  users = session.query(User).all()
  return users


def query_by_username(name):
  users= session.query(
    User).filter_by(
    name=name).first()
  return users 

def query_by_password(password):
  users= session.query(
    User).filter_by(
    password=password).all()
  return users   


# def check_login(name,password):
# 	user= session.query(
#     User).filter_by(
#     name=name, password=password).first()
#     if user is not None:
#     	return True
#     return False