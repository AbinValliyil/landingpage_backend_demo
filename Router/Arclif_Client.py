from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session
from Security.jwt_bearer import JWTBearer


router=APIRouter()
db = SessionLocal()


@router.post('/cleint_details',dependencies=[Depends(JWTBearer())],tags=['CLIENT'])
def create_user_details( client:schemas.Arclif_client_details, user_id:str,db: session = Depends(get_db)):
    
    user = db.query(models.Client_Details).filter(models.Client_Details.mobile_number==client.mobile_number).first()
    user1 = db.query(models.Client_Details).filter(models.Client_Details.email==client.email).first()
    
    if user is not None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="mobile allready exixt")

        #  return{"error_message": "There was a problem with your login","status":status.HTTP_404_NOT_FOUND}
    elif user1 is not None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="email allready exixt")

    new_client = models.Client_Details(**client.dict(),owner_id=user_id)
    db.add(new_client)
    db.commit()
    return client
    




@router.post('/cleint_requirements',dependencies=[Depends(JWTBearer())],tags=['CLIENT'])
def create_user_requirements( client:schemas.Requirements_Create, user_id:str,db: session = Depends(get_db)):
    
    new_client = models. Client_Requirements(**client.dict(),owner_id=user_id)
    db.add(new_client)
    db.commit()
    return client





@router.put('/Update_cleint_requirements',dependencies=[Depends(JWTBearer())],tags=['CLIENT'])
def create_user_requirements( client:schemas.Requirements_Create, user_id:str,db: session = Depends(get_db)):
    
    new_client = db.query(models.Client_Requirements).filter(models.Client_Requirements.owner_id==user_id).first()
    if not new_client :
        return 'first you put details then update'
    
    new_client.totoal_budget         =    client.totoal_budget
    new_client.total_area            =    client.total_area 
    new_client.floor_number          =    client.floor_number
    new_client.design                =    client.design
    new_client.common_bedrooms       =    client.common_bedrooms
    new_client.attached_bedrooms     =    client.attached_bedrooms
    new_client.family_members        =    client.family_members
    new_client.outside_washrooms     =    client.outside_washrooms
    new_client.inside_washrooms      =    client.inside_washrooms
    new_client.attacheed_washrooms   =    client.attacheed_washrooms

    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return client
   