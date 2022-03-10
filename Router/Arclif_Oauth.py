from fastapi import APIRouter, Depends,status,HTTPException,Response
from Model.models import ArclifUser
from Model import schemas,models
from Security.jwt_handler import signJWT
from Security.utils import verify,hash
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session
from fastapi import Request, HTTPException
from Security.jwt_bearer import JWTBearer
from fastapi.responses import JSONResponse


router=APIRouter()
db = SessionLocal()


@router.post('/create_user',tags=['OAUTH'])

async def create_an_user(user:schemas.Arclif_SingUp,db:session=Depends(get_db)):
    
    
    db_user_num= db.query(ArclifUser).filter(models.ArclifUser.mobile_number ==user.mobile_number).first()
    
  
    if  db_user_num  is not  None:
        raise HTTPException(detail="mobile  number already exists!",status_code=404)

    token =signJWT(user.mobile_number)

    new_user = models.ArclifUser(**user.dict())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    f_id = db.query(models.ArclifUser.id).filter(models.ArclifUser.mobile_number==user.mobile_number).first()
    return {
        'status':"true",
         **f_id,
        'name'    :user.name,
        'mob'     :user.mobile_number,
        'token'  :token
        
    }


@router.post('/login',tags=['OAUTH'])
def user_login(user_credentials:schemas.ArclifUser_login,db:session=Depends(get_db)):
    user = db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number==user_credentials.mobile_number).first()
    
    if  user is  None:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There was a problem with your login")

    

    token =signJWT(user.mobile_number)

    return  {
       'status'         :"true",
       'mob'            :user_credentials.mobile_number,
       'user'           :user.name ,
       'user_id'        :user.id,
       'token'          :token

    }


    
# @router.post("/cookie/",tags=['SET-COOKIE'])
# def create_cookie(mobile_number:str,password = None):
#     token1 = signJWT( mobile_number )
#     content = {"message": "Come to the dark , we have cookies"}
#     response = JSONResponse(content=content)
#     response.set_cookie(key="Bearer",value=token1,expires=60,httponly=True,samesite=None,secure=True)
#     return response


  


# @router.put('/Reset_password',tags=["OAUTH"])
# async def reset(user:schemas.ArclifUser_login,db:session=Depends(get_db)):
    
#     users = db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number==user.mobile_number).first()
    
#     if not users:

    
#      return{"error_message": "There was a problem with your password reset","status":status.HTTP_404_NOT_FOUND}
    
#     hashed_password = hash(user.password)
#     users.password  = hashed_password
    
#     token = signJWT( user.mobile_number )
    

#     db.add(users)
#     db.commit()
#     db.refresh(users)

    
#     return  {"message":"password reset success ",'user_data':{

#                 'status'         :200,
#                 'id'             :users.id,
#                 'name'           :users.name,
#                 'mobile_number'  : user.mobile_number,
#                 "access_token"   :token,  
#                 "token_type"     :"Bearer",
#                 'status'         :status.HTTP_302_FOUND }}
    



