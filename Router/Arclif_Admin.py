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


@router.put('/sql_update',tags=['ADMIN']) 
async def sql_up(new:schemas.Sqt_price,db:session=Depends(get_db)):
    new_sqt= db.query(models.Sqt).filter(models.Sqt.id==1).first()
    if not new_sqt:
        new_sqt = models.Sqt(**new.dict())
        db.add(new_sqt)
        db.commit()
        db.refresh(new_sqt)
        return new_sqt
        
    #new_sqt =models.Sqt(silver=s,golden=g,platinum=p)
    new_sqt.silver    =  new.silver
    new_sqt.golden    =  new.golden
    new_sqt.platinum  =  new.platinum
    db.add(new_sqt)
    db.commit()
    db.refresh(new_sqt)
    return new_sqt

@router.put('/sql_pstg_update',tags=['ADMIN']) 
async def sql_up(new:schemas.Sqt_price,db:session=Depends(get_db)):
    new_sqt= db.query(models.Sqt).filter(models.Sqt.id==2).first()
    if not new_sqt:
        new_sqt = models.Sqt(**new.dict())
        db.add(new_sqt)
        db.commit()
        db.refresh(new_sqt)
        return new_sqt
        
    #new_sqt =models.Sqt(silver=s,golden=g,platinum=p)
    new_sqt.silver    =  new.silver
    new_sqt.golden    =  new.golden
    new_sqt.platinum  =  new.platinum
    db.add(new_sqt)
    db.commit()
    db.refresh(new_sqt)
    return new_sqt
