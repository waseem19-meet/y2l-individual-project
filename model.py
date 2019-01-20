from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
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
	user_id = Column(Integer, ForeignKey('user.id'))

	def __repr__(self):
		return ("Subject: {}, offer content:{}".format(self.subject, self.content))




class User(Base):
  __tablename__="user"
  id=Column(Integer, primary_key=True)
  status=Column(String)
  name=Column(String, unique=True )
  email=Column(String)
  password=Column(String)
  PhoneNum=Column(Integer)

  def __repr__(self):
  	return ("user status: {}, user name:{}, user email:{}, user password:{}, user Phone Num:{}".format(self.status, self.name, self.email,self.password, self.PhoneNum))
 
  


  
	   

