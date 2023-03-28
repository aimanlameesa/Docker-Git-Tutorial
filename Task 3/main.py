# Import the required libraries
from fastapi import FastAPI, Request
# import requests
import base64
# import json

app = FastAPI()
# BASE64_API = "http://localhost:8000/base64"

@app.get("/")
async def root(name= "Aiman"):

    # Enter name
    # name = input("Enter your name: ")
    
    if name == "Aiman":
        name_bytes = name.encode('utf-8')
        base64_bytes = base64.b64encode(name_bytes)
        base64_name = base64_bytes.decode('utf-8')
        return f"Base64-encoded name: {base64_name}"
    else:
        print("Error: API call failed!")

# @app.get("/hello")
# async def hello():
#   return {"Welcome!"}