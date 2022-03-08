from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session




router=APIRouter()
db = SessionLocal()

@router.get('/silver_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
    g =int(new.silver)
    v =g*sqt
    return {'silver_package':v}


@router.get('/Golden_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
    g=int(new.golden)
    v =g*sqt
    return {'Golden_package':v}



@router.get('/paltinum_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
    g =int(new.platinum)
    v =g*sqt
 
    return {'paltinum_package':v}
    

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


