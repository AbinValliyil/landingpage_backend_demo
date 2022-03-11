from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from Security.Random_OTP import OTPgenerator
import requests
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session
from decouple import config



API = config("OTP_API")



router=APIRouter()
db = SessionLocal()



    
@router.post('/OTP_Genarator/singup',tags=['MOBILE_OTP'])
async def otp(mobile_num:str,db:session=Depends(get_db)):
    db_user= db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number ==mobile_num).first()

    if db_user is not  None:
        # raise HTTPException(status_code=400,error_message="mobile number already exists!")
        #return JSONResponse(status_code=400,content="mobile number already exists!")
        return{"error_message": "mobile number already exists !","status":status.HTTP_400_BAD_REQUEST}
           
    url ="https://www.fast2sms.com/dev/bulkV2"
    otp = OTPgenerator()
    mobile_number =mobile_num
    payload = f"variables_values={otp} , Team  ARCLIF ! &route=otp&numbers={mobile_number}"
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


    return {"status":status.HTTP_202_ACCEPTED,"mob":mobile_number} 

  

@router.post('/OTP_Genarator/login',tags=['MOBILE_OTP'])
async def otp(mobile_num:str,db:session=Depends(get_db)):
    db_user= db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number ==mobile_num).first()

    if db_user is   None:
        return{"error_message": "Can't find your account try sing-up or check your Mobile number! ","status":status.HTTP_404_NOT_FOUND}
    
        # raise HTTPException(status_code=400,error_message="mobile number already exists!")
        #return JSONResponse(status_code=400,content="mobile number already exists!")
        # return{"error_message": "mobile number Ethalladoo !! ni poi singup cheyy ! please --> Singup","status":status.HTTP_400_BAD_REQUEST}
    url ="https://www.fast2sms.com/dev/bulkV2"
    otp = OTPgenerator()
    mobile_number =mobile_num
    payload = f"variables_values={otp} , Team ARCLIF ! &route=otp&numbers={mobile_number}"
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

   

    return {"status":status.HTTP_202_ACCEPTED,"mob":mobile_number} 
    

@router.post('/otp_verification',tags=['MOBILE_OTP'])
def otp_verification(mobile:str,otp:str,db:session=Depends(get_db)):
     
    
    valid_otps = db.query(models.ARCLIF_OTP.otp).filter(models.ARCLIF_OTP.mobile_number==mobile).all()
    
    
    

    if valid_otps:
        valid_otp =list(valid_otps).pop()
        if valid_otp[0] == otp:

            return {"message":"OTP Verification Successfull","status":status.HTTP_202_ACCEPTED}

             
    return {"message":"Invalid OTP","status":status.HTTP_404_NOT_FOUND}
    

