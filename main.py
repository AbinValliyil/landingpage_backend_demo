from fastapi import FastAPI
from  fastapi  import FastAPI,Depends,status
from DB.db import Base, engine
from Model import models
from Router import Arclif_user
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
    "pulic.vercel"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(Arclif_user.router)

@app.get('/')
async def server():
      return 'server ready for arclif'




