from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_offer(subject, content, user_id):
    print("Added an offer!")
    offer = Offer(subject=subject, content=content)
    session.add(offer)
    session.commit()


def get_all_offers():
  offers = session.query(Offer).all()
  return offers



def add_user(status, name, email, password):
    print("Added a user!")
    user = User(status=status, name=name, email=email, password=password)
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