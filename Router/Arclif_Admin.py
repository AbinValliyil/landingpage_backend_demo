from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session
from Security.jwt_bearer import JWTBearer


router=APIRouter()
db = SessionLocal()


@router.get('/gcleint_requirements',dependencies=[Depends(JWTBearer())],tags=['ADMIN'])
def create_user_requirements(user_id:str,db: session = Depends(get_db)):
    my_client = db.query(models.Client_Requirements).filter(models.Client_Requirements.owner_id==user_id).all()
    client =my_client.pop()

    return client


@router.get('/all_cleint',dependencies=[Depends(JWTBearer())],tags=['ADMIN'])
async def getclient(db: session = Depends(get_db)):
    my_client = db.query(models.ArclifUser).all()
    
    return my_client