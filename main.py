from fastapi import FastAPI
from  fastapi  import FastAPI,Depends,status
from DB.db import Base, engine
from Model import models
from Router import Sqft_price,Arclif_Admin,Arclif_Client,Arclif_Oauth,Payment,Mobile,Email,RONE
from fastapi.middleware.cors import CORSMiddleware
# from  Security.jwt_bearer import JWTBearer

models.Base.metadata.create_all(bind=engine)# automatic Database table create  


app=FastAPI( title="Arclif" ,

  contact={
        "name": "Abin_michael",

        "email": "abinvalliyil@gmail.com"
             
                          })



origins = [
    "http://localhost:3000",
    "https://architectural-services-arclifs.vercel.app",
    "https://rone-demo.vercel.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(Arclif_Oauth.router)
app.include_router(Arclif_Client.router)
app.include_router(Sqft_price.router)
app.include_router(Arclif_Admin.router)
app.include_router(Mobile.router)
app.include_router(Payment.router)
app.include_router(Email.router)
app.include_router(RONE.router)
@app.get('/',tags=['SERVER'])
async def server():
      return 'server ready for arclif'




