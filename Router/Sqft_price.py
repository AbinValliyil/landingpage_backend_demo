from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session




router=APIRouter()
db = SessionLocal()

@router.get('/silver_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
    new_sqt_p=db.query(models.Sqt).filter(models.Sqt.id==2).first()
    if  not new:
        return 'Not fixed this amount'

    if  not new_sqt_p:
        return 'Not fixed this amount'

    sqt_p =int(new_sqt_p.silver)
    g =int(new.silver)
    v =g*sqt
    p = v/sqt_p
    return {'silver_package':v,f'Advance_payment at {sqt_p}%':p}


@router.get('/Golden_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
    
    new_sqt_p=db.query(models.Sqt).filter(models.Sqt.id==2).first()

    if  not new:
        return 'Not fixed this amount'
   
    if  not new_sqt_p:
        return 'Not fixed this amount'

    sqt_p =int(new_sqt_p.golden)

    g=int(new.golden)
    v =g*sqt
    p = v/sqt_p
    return {'Golden_package':v,f'Advance_payment at {sqt_p}%':p}



@router.get('/paltinum_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
    new_sqt_p=db.query(models.Sqt).filter(models.Sqt.id==2).first() 

    if  not new:
        return 'Not fixed this amount'
    
    if  not new_sqt_p:
        return 'Not fixed this amount'

    sqt_p =int(new_sqt_p.platinum)

    g =int(new.platinum)
    v = g*sqt
    p = v/sqt_p
 
    return {'paltinum_package':v,f'Advance_payment at {sqt_p}%':p}


