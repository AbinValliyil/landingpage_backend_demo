from cmath import e
from urllib import response
from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from Security.Random_OTP import OTPgenerator
import requests,time,datetime
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session
from decouple import config
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import aiofiles



API = config("OTP_API")



router=APIRouter()
db = SessionLocal()




# THIS APIS FOR RONE  PROJECT

from fastapi.responses import FileResponse
from os import getcwd, remove
from fastapi.responses import JSONResponse



@router.post('/OTP_Genarator/rone/singup',tags=['RONE'])
async def otp(mobile_num:str,db:session=Depends(get_db)):
    db_user= db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number ==mobile_num).first()
    
    if db_user is not  None:
     
        return{"error_message": "mobile number already exists !","status":status.HTTP_400_BAD_REQUEST}
           
    url ="https://www.fast2sms.com/dev/bulkV2"
    otp =  OTPgenerator()
    mobile_number =mobile_num
    payload = f"variables_values={otp} , Team RONE ! &route=otp&numbers={mobile_number}"
    headers = {
    'authorization':API,
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }  
    
    response = requests.request("POST", url, data=payload, headers=headers)
    if not response:
        return{"status":status.HTTP_503_SERVICE_UNAVAILABLE}
    
     
    new_otp =models.ARCLIF_OTP(mobile_number=mobile_num,otp=otp)
    db.add(new_otp)
    db.commit()
    db.refresh(new_otp)
    

    return {"status":status.HTTP_202_ACCEPTED,"mob":mobile_number,'id':new_otp.id} 

  

@router.post('/OTP_Genarator/rone/login',tags=['RONE'])
async def otp(mobile_num:str,db:session=Depends(get_db)):
    db_user= db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number ==mobile_num).first()

    if db_user is   None:
        return{"error_message": "Can't find your account try sing-up or check your Mobile number! ","status":status.HTTP_404_NOT_FOUND}
    
    url ="https://www.fast2sms.com/dev/bulkV2"
    otp = OTPgenerator()
    payload = f"variables_values={otp} , Team  RONE  ! &route=otp&numbers={mobile_num}"
    headers = {
    'authorization':API,
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }  
    
    response = requests.request("POST", url, data=payload, headers=headers)
    if not response:

        return{"status":status.HTTP_503_SERVICE_UNAVAILABLE}
    
    new_otp =models.ARCLIF_OTP(mobile_number=mobile_num,otp=otp)
    db.add(new_otp)
    db.commit()
    db.refresh(new_otp)
   
    return {"status":status.HTTP_202_ACCEPTED,"mob":mobile_num,'id':new_otp.id}
    


