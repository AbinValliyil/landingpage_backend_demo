from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config




#local database

# engine=create_engine('postgresql://postgres:123@localhost/Arclif',echo=True) 


#heroku database


DB='DB_URL'

engine =create_engine( config( DB))


print("Database ****** connected")

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


SessionLocal=sessionmaker(bind = engine)
