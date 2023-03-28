from PIL import Image, ImageDraw
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import base64
import io

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    # Read input image
    with open("cat.jpeg", "rb") as f:
        img = Image.open(io.BytesIO(f.read()))

    # Define bounding box coordinates
    x1, y1, x2, y2 = 150, 85, 350, 200

    # Get dimensions of input image
    img_w, img_h = img.size

    # Check if bounding box is valid
    if x1 < 0 or y1 < 0 or x2 > img_w or y2 > img_h:
        print("Invalid bounding box!")

    else:

        # Draw bounding box on input image
        draw = ImageDraw.Draw(img)
        draw.rectangle([x1, y1, x2, y2], outline=(0, 255, 0), width=2)

        # Display output image
        # img.show()

        # Convert image to JPEG format
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format='JPEG')
        img_byte_array = img_byte_array.getvalue()

        # Convert JPEG image data to base64 encoded string
        img_base64 = base64.b64encode(img_byte_array).decode()

        # Embed base64 encoded image string in HTML
        html = f"<img src='data:image/jpeg;base64,{img_base64}'>"

        return html