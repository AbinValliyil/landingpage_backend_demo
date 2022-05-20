import smtplib,ssl
from fastapi import APIRouter, Depends,status,HTTPException
from Model import schemas,models
from Security.Random_OTP import OTPgenerator
import requests,time,datetime
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session
from decouple import config



router=APIRouter()
db = SessionLocal()






@router.get('/email',tags =['Email'])
async def email():
#    server = smtplib.SMTP(',587)
   
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   
    
   try:

        server.login('@gmail.com','password')
         
   except:
        return 404
   try:
        
         server.sendmail("sender","reciver",'Hello its python ')

         server.quit()
   except:
        
        return 406

   return 'ok'
