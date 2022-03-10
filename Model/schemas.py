from os import name
from pydantic import BaseModel






#signup model

class Arclif_SingUp(BaseModel):
    name           :str
    mobile_number  :str


class config:
    orm_mode = True



# login model


class ArclifUser_login(BaseModel):

    mobile_number:str

    class config:
        orm_mode = True



class Arclif_client(BaseModel):
    name:str
    mobile_number:str
    city:str
    state:str
    pin_number:str
    profession  :str
    family_members :int
    sinior_citzen  :bool
    
class Arclif_client_details(Arclif_client):
    pass


class Rel(Arclif_client):
    id             :int
    owner_id       :int
     
    class Config:
        orm_mode = True




class Client(BaseModel):
 totoal_budget        :str
 total_area           :str
 floor_number         :str
 design               :str
 common_bedrooms      :str
 attached_bedrooms    :str
 family_members       :str
 outside_washrooms    :str
 inside_washrooms     :str
 attacheed_washrooms  :str


class Requirements_Create(Client):
    pass


class rq(Client):
    id             :int
    owner_id       :int
     
    class Config:
        orm_mode = True

class Sqt_price(BaseModel):
    silver    :int
    golden    :int
    platinum  :int

    class Config:
        orm_mode = True
