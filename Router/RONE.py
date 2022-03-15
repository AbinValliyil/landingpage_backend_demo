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

path ='/SRC'

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
    


@router.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):
    print("filename = ", file.filename) # getting filename
    destination_file_path = "Static/image"+file.filename # location to store file
    async with aiofiles.open(destination_file_path, 'wb') as out_file:
        while content := await file.read(1024):  # async read file chunk
            await out_file.write(content)  # async write file chunk

    return {"Result": "OK",'path':destination_file_path,"filenames": file.filename}



@router.get("/download-file")
def download_file():
    file_path = "Static/imageScreenshot (101).png"
    return FileResponse(path=file_path, filename=file_path)


@router.post("/upload-files")
async def create_upload_files(files: list[UploadFile] = File(...)):
    for file in files:
        destination_file_path = "Static/image"+file.filename #output file path
        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while content := await file.read(1024):  # async read file chunk
                await out_file.write(content)  # async write file chunk

    return {"Result": "OK", "filenames": [file.filename for file in files]}


# @router.get("/res-file")
# def download_file(file_name:str):
#     return FileResponse(getcwd() +'/'+ file_name)
@router.delete("/delete/file/{name_file}")
def delete_file(name_file: str):
    try:
        remove(getcwd() + "/" + name_file)
        return JSONResponse(content={
            "removed": True
            }, status_code=200)   
    except FileNotFoundError:
        return JSONResponse(content={
            "removed": False,
            "error_message": "File not found"
        }, status_code=404)

@router.get('/img')
async def d():
   
    return FileResponse('Static\imageIMG_20220301_174007.jpg')
    