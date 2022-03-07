from http import client
from sqlalchemy import null
from fastapi import APIRouter, Depends,status,HTTPException,Response
from Model.models import ArclifUser
from Model import schemas,models
from Security.jwt_handler import signJWT
from Security.utils import verify,hash
from DB.db import Base, engine,get_db ,SessionLocal
from sqlalchemy.orm import session
from fastapi import Request, HTTPException
from Security.jwt_bearer import JWTBearer


router=APIRouter()
db = SessionLocal()


@router.post('/create_user',tags=['USER'])

async def create_an_user(user:schemas.Arclif_SingUp,db:session=Depends(get_db)):
    
    
    db_user_num= db.query(ArclifUser).filter(models.ArclifUser.mobile_number ==user.mobile_number).first()
    db_user_email= db.query(ArclifUser).filter(models.ArclifUser.email==user.email).first()
  
    if  db_user_num  is not  None:
        raise HTTPException(detail="mobile  number already exists! !",status_code=404)
        #return JSONResponse(status_code=400,content="mobile number already exists!")
        # return{"error_message": "mobile or email number already exists!","status":status.HTTP_400_BAD_REQUEST}
        
    elif  db_user_email  is not  None:
        # raise HTTPException(status_code=400,error_message="mobile number already exists!")
        #return JSONResponse(status_code=400,content="mobile number already exists!")
        # return{"error_message": "mobile or email number already exists!","status":status.HTTP_400_BAD_REQUEST}
        raise HTTPException(detail=" email_id already exists! !",status_code=404)
    else:

      hashed_password = hash(user.password)
      user.password = hashed_password
      
    
      token =signJWT(user.mobile_number)

      new_user = models.ArclifUser(**user.dict())
    
      db.add(new_user)
      db.commit()
      db.refresh(new_user)
      f_id = db.query(models.ArclifUser.id).filter(models.ArclifUser.mobile_number==user.mobile_number).first()
      return {
        **f_id,
        'name'    :user.name,
        'email'   :user.email,
        'mob'     :user.mobile_number,
        '1token'  :token
        
    }


@router.post('/login',tags=['USER'])
def user_login(user_credentials:schemas.ArclifUser_login,db:session=Depends(get_db)):
    user = db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number==user_credentials.mobile_number).first()
    
    if  user is  None:


    
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There was a problem with your login")

        #  return{"error_message": "There was a problem with your login","status":status.HTTP_404_NOT_FOUND}
    
    if not verify(user_credentials.password,user.password):
              raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="There was a problem with your login")

    token =signJWT(user.mobile_number)

    return  {

       'mob': user_credentials.mobile_number,
       'user':user.name ,
       'user_id':user.id,
       'token':token

    }


  


@router.put('/Reset_password',tags=["USER"])
async def reset(user:schemas.ArclifUser_login,db:session=Depends(get_db)):
    
    users = db.query(models.ArclifUser).filter(models.ArclifUser.mobile_number==user.mobile_number).first()
    
    if not users:

    
     return{"error_message": "There was a problem with your password reset","status":status.HTTP_404_NOT_FOUND}
    
    hashed_password = hash(user.password)
    users.password  = hashed_password
    
    token = signJWT( user.mobile_number )
    

    db.add(users)
    db.commit()
    db.refresh(users)

    
    return  {"message":"password reset success ",'user_data':{

                'id'             :users.id,
                'name'           :users.name,
                'mobile_number'  : user.mobile_number,
                "access_token"   :token,  
                "token_type"     :"Bearer",
                'status'         :status.HTTP_302_FOUND }}
    




@router.post('/cleint_details',dependencies=[Depends(JWTBearer())],tags=['CLIENT_DETAILS'])
def create_user_requirements( client:schemas.Arclif_client_details, user_id:str,db: session = Depends(get_db)):
    
    user = db.query(models.Client_Details).filter(models.Client_Details.mobile_number==client.mobile_number).first()
    user1 = db.query(models.Client_Details).filter(models.Client_Details.email==client.email).first()
    print(user)
    if user is not None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="mobile allready exixt")

        #  return{"error_message": "There was a problem with your login","status":status.HTTP_404_NOT_FOUND}
    elif user1 is not None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="email allready exixt")

    new_client = models.Client_Details(**client.dict(),owner_id=user_id)
    db.add(new_client)
    db.commit()
    return client
    




@router.post('/cleint_requirements',dependencies=[Depends(JWTBearer())],tags=['CLIENT_REQUEREMWENTS'])
def create_user_requirements( client:schemas.Requirements_Create, user_id:str,db: session = Depends(get_db)):
    
    new_client = models. Client_Requirements(**client.dict(),owner_id=user_id)
    db.add(new_client)
    db.commit()
    return client





@router.put('/Update_cleint_requirements',dependencies=[Depends(JWTBearer())],tags=['CLIENT_REQUEREMWENTS'])
def create_user_requirements( client:schemas.Requirements_Create, user_id:str,db: session = Depends(get_db)):
    
    new_client = models. Client_Requiremets(**client.dict(),owner_id=user_id)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return client



@router.get('/gcleint_requirements',dependencies=[Depends(JWTBearer())],tags=['CLIENT_REQUEREMWENTS'])
def create_user_requirements(user_id:str,db: session = Depends(get_db)):
    my_client = db.query(models.Client_Details).filter(models.Client_Details.owner_id==user_id).all()
    
    return my_client


@router.get('/all_cleint',dependencies=[Depends(JWTBearer())],tags=['ALL_CLIENTS'])
async def getclient(db: session = Depends(get_db)):
    my_client = db.query(models.ArclifUser).all()
    
    return my_client