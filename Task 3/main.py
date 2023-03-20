# Import the required libraries
from fastapi import FastAPI, Request
import base64

app = FastAPI()

@app.get("/hello")
async def hello(request: Request):

    # Enter name
    name = input("Enter your name: ")
    
    if name == "Aiman":
        name_bytes = name.encode('utf-8')
        base64_bytes = base64.b64encode(name_bytes)
        base64_name = base64_bytes.decode('utf-8')
        return f"Base64-encoded name: {base64_name}"
    else:
        return "Sorry, that is an incorrect name."

# @app.get("/hello")
# async def hello():
#   return {"Welcome!"}