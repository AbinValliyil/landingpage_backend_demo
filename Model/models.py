import string
from DB.db import Base
from sqlalchemy import String,Boolean,Integer,Column,DateTime,ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from typing import Text
from sqlalchemy.orm import  relationship


class ArclifUser(Base):
    __tablename__='arclif_users'
    id                = Column(Integer,primary_key=True,autoincrement=True)
    name              = Column(String,nullable=False)
    mobile_number     = Column(String,nullable=False,unique=True)
    created_at        = Column(DateTime, default=current_timestamp())
    updated_at        = Column(DateTime, onupdate=current_timestamp())
    user_details      = relationship("Client_Details", back_populates="owner")
    client_req        = relationship("Client_Requirements", back_populates="owner")

class Client_Details(Base):
    __tablename__ ='client_details'
    id                = Column(Integer,primary_key=True,autoincrement=True)
    name              = Column(String,nullable=False)
    mobile_number     = Column(String,nullable=False)
    city              = Column(String,nullable=False)
    state             = Column(String,nullable=False)
    pin_number        = Column(String,nullable=False)
    profession        = Column(String,nullable=False)
    family_members    = Column(Integer,nullable=False)
    sinior_citzen     = Column(Boolean,nullable=False)
    owner_id          = Column(Integer, ForeignKey("arclif_users.id"))
    owner             = relationship("ArclifUser", back_populates="user_details")
    created_at        = Column(DateTime, default=current_timestamp())
    updated_at        = Column(DateTime, onupdate=current_timestamp())


 

class Client_Requirements(Base):
    __tablename__ ='client_requirements'
    id                   = Column(Integer,primary_key=True,autoincrement=True)
    totoal_budget        = Column(String,nullable=False)
    total_area           = Column(String,nullable=False)
    floor_number         = Column(String,nullable=False)
    design               = Column(String,nullable=False)
    common_bedrooms      = Column(String,nullable=False)
    attached_bedrooms    = Column(String,nullable=False)
    family_members       = Column(String,nullable=False)
    outside_washrooms    = Column(String,nullable=False)
    inside_washrooms     = Column(String,nullable=False)
    attacheed_washrooms  = Column(String,nullable=False)
    owner_id             = Column(Integer, ForeignKey("arclif_users.id"))
    owner                = relationship("ArclifUser", back_populates="client_req")
    created_at           = Column(DateTime, default=current_timestamp())
    updated_at           = Column(DateTime, onupdate=current_timestamp())



class Sqt(Base):
    __tablename__ ='sqt_price'
    id            = Column(Integer,primary_key=True,autoincrement=True)
    silver        = Column(Integer,nullable=False)
    golden        = Column(Integer,nullable=False)
    platinum      = Column(Integer,nullable=False)
                        





class ARCLIF_OTP(Base):
    __tablename__='otp'
    id                = Column(Integer,primary_key=True,autoincrement=True)
    mobile_number     = Column(String,nullable=False)
    otp               = Column(String,nullable=False)
    created_at        = Column(DateTime, default=current_timestamp())
    updated_at        = Column(DateTime, onupdate=current_timestamp())
