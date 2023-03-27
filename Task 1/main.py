from fastapi import FastAPI
import csv

app = FastAPI()

@app.get("/")
async def root():
    # open .tsv file
    with open("sample.tsv") as file:
        # Passing the TSV file to 
        # reader() function
        # with tab delimiter
        # This function will
        # read data from file
        tsv_file = csv.reader(file, delimiter="\t")
        
        store = []

        # line = []
        # printing data line by line
        for line in tsv_file:
            # store.append(line)
            stripped_list = [s.strip() for s in line]
            stripped_list = list(filter(None, stripped_list))
            output_str = ", ".join(stripped_list)
            store.append(output_str)

        return store




# Import the required libraries
#from PIL import Image
# from fastapi import FastAPI
#from fastapi.responses import HTMLResponse
#import numpy as np
#import cv2
#import base64

# app = FastAPI()

# @app.get("/")
# async def root():
    # return {"message": "AICenter Welcomes you!"}

# @app.get("/", response_class=HTMLResponse)
# async def hello():
#     # Read input image
#     img = cv2.imread("cat.jpeg")

#     # Define bounding box coordinates
#     x1, y1, x2, y2 = 150, 85, 350, 200

#     # Get dimensions of input image
#     img_h, img_w = img.shape[:2]

#     # Check if bounding box is valid
#     if x1 < 0 or y1 < 0 or x2 > img_w or y2 > img_h:
#         print("Invalid bounding box!")

#     else:

#         # Draw bounding box on input image
#         cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)

#         # Display output image
#         # cv2.imshow("Output Image", img)
#         # cv2.waitKey(0)
       
#         # Convert image to JPEG format
#         _, img_encoded = cv2.imencode(".jpeg", img)

#         # Convert JPEG image data to base64 encoded string
#         img_base64 = base64.b64encode(img_encoded).decode()

#         # Embed base64 encoded image string in HTML
#         html = f"<img src='data:image/jpeg;base64,{img_base64}'>"

#         return html

# @app.get("/hello")
# async def hello():	
# 	return {"Welcome!"}
