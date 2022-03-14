from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session




router=APIRouter()
db = SessionLocal()



async def package_sqt():
   new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
   new_sqt_p=db.query(models.Sqt).filter(models.Sqt.id==2).first()
   if  not new:
        return 'Not fixed this amount'
   if  not new_sqt_p:
        return 'Not fixed this amount'

    
   return {
           'silver':new.silver,'golden':new.golden,'platinum':new.platinum,
           'silver_ptg':new_sqt_p.silver,'golden_ptg':new_sqt_p.golden,'platinum_ptg':new_sqt_p.platinum
        }
    
async def pack_sqts():
    return await package_sqt()


@router.get('/silver_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
  
    f = await package_sqt()
    silver_pack_price       = f['silver']
    silver_pack_percentage  = f['silver_ptg']
    amount =int(silver_pack_price)*sqt
    total =amount/int(silver_pack_percentage)
    return {'sqt':sqt,'total':amount,'down_pay':total,'down_payment':str(silver_pack_percentage)+'%'}



@router.get('/Golden_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    f = await package_sqt()
    silver_pack_price       = f['golden']
    silver_pack_percentage  = f['golden_ptg']
    amount =int(silver_pack_price)*sqt
    total =amount/int(silver_pack_percentage)
    return {'sqt':sqt,'total':amount,'down_pay':total,'down_payment':str(silver_pack_percentage)+'%'}

  



@router.get('/paltinum_package_price',tags=['PACKAGE_PRICE'])
async def sqt_cal(sqt:int):
    f = await package_sqt()
    silver_pack_price       = f['platinum']
    silver_pack_percentage  = f['platinum_ptg']
    amount =int(silver_pack_price)*sqt
    total =amount/int(silver_pack_percentage)
    return {'sqt':sqt,'total':amount,'down_pay':total,'down_payment':str(silver_pack_percentage)+'%'}
   



# @router.get('/paltinum_package_price',tags=['PACKAGE_PRICE'])
# async def sqt_cal(sqt:int):
#     new = db.query(models.Sqt).filter(models.Sqt.id==1).first()
#     new_sqt_p=db.query(models.Sqt).filter(models.Sqt.id==2).first() 

#     if  not new:
#         return 'Not fixed this amount'
    
#     if  not new_sqt_p:
#         return 'Not fixed this amount'

#     sqt_p =int(new_sqt_p.platinum)

#     g =int(new.platinum)
#     v = g*sqt
#     p = v/sqt_p
 
#     return {'paltinum_package':v,f'Advance_payment at {sqt_p}%':p}
