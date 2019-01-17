from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Offer(Base):
    __tablename__ = "offer"
    id = Column(Integer, primary_key = True)
    subject = Column(String)
    content= Column(String)
    # user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return ("Subject: {}, offer content:{}".format(self.subject, self.content))




class User(Base):
  __tablename__="user"
  id=Column(Integer, primary_key=True)
  name=Column(String, unique=True )
  email=Column(String)
  password=Column(String)
 
  


  def __repr__(self):
    return ("user name:{}, user email:{} user password:{}".format(self.name, self.email,self.password))
       

