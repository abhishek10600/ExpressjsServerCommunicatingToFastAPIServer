from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import requests
import json
import os
from dotenv import load_dotenv
from models.userModel import UserModel

load_dotenv()

server1_url = os.getenv("SERVER1_URL")

app = FastAPI()

origins = [
    server1_url
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post("/user/get-data")
async def get_user_data(user_data: UserModel):
    data = jsonable_encoder(user_data)
    print(data)
    print(data["name"])
    print(data["email"])
    print(data["password"])
    return {
        "success": True,
        "message": "data recieved",
        "data": data
    }
