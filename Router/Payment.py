from fastapi import APIRouter,status,Depends

import requests
from Model import schemas,models
from sqlalchemy.orm import session
from decouple import config
import razorpay

router=APIRouter()


    
@router.post('/payment',tags=['PAYMENT_GATEWAY'])
async def pay(RS:int):
    client = razorpay.Client(auth=("rzp_test_gy2OEpQuEEknY6", "oQUFyPYVObMGkHmgJu5o2P94"))
    data = { "amount": RS, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    return payment
    