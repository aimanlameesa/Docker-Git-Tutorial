# Import the required libraries
from PIL import Image
from fastapi import FastAPI
import numpy as np
import cv2

app = FastAPI()

@app.get("/hello")
async def hello():
    # Read input image
    img = cv2.imread("cat.jpeg")

    # Define bounding box coordinates
    x1, y1, x2, y2 = 150, 85, 350, 200

    # Get dimensions of input image
    img_h, img_w = img.shape[:2]

    # Check if bounding box is valid
    if x1 < 0 or y1 < 0 or x2 > img_w or y2 > img_h:
        print("Invalid bounding box!")

    else:

        # Draw bounding box on input image
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)

        # Display output image
        cv2.imshow("Output Image", img)
        cv2.waitKey(0)

# @app.get("/hello")
# async def hello():
#   return {"Welcome!"}