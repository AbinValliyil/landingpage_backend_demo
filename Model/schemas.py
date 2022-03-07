from os import name
from pydantic import BaseModel





#signup model

class Arclif_SingUp(BaseModel):
    name           :str
    mobile_number  :str
    email          :str
    password       :str


class config:
    orm_mode = True



# login model


class ArclifUser_login(BaseModel):

    mobile_number:str
    password     :str

    class config:
        orm_mode = True



class Arclif_client(BaseModel):
    name:str
    mobile_number:str
    email:str
    city:str
    state:str
    pin_number:str
    profession  :str
    family_members :int
    
class Arclif_client_details(Arclif_client):
    pass


class Rel(Arclif_client):
    id             :int
    owner_id       :int
     
    class Config:
        orm_mode = True




class Client(BaseModel):
 totoal_budget        :int
 total_area           :str
 floor_number         :int
 design               :str
 common_bedrooms      :int
 attached_bedrooms    :int
 family_members       :int
 outside_washrooms    :int
 inside_washrooms     :int
 attacheed_washrooms  :int


class Requirements_Create(Client):
    pass


class rq(Client):
    id             :int
    owner_id       :int
     
    class Config:
        orm_mode = True

