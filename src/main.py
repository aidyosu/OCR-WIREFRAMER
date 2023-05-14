import uvicorn
import importlib

from typing import Optional
from fastapi import FastAPI, File, UploadFile, Request

# Load the required packages and the ONNX model
import io
from PIL import Image
import numpy as np
from paddleocr import PaddleOCR,draw_ocr
from src.utils import bbox_norm

app = FastAPI()



# Add your FastAPI routes and functions below
@app.get("/")
async def root():
    return {"message": "Hello World"}


# Defining the endpoint that will receive the image file and perform predictions
@app.post("/generate")
async def results(request:Request, file: UploadFile = File(...) ):
    # Read the image file into memory
    # Read only image files

    
    # read the uploaded image file
    # print the OCR results


    contents = await file.read()
    image_np = Image.open(io.BytesIO(contents)).convert('RGB')
    image = np.array(image_np)

    # Apply the image transformations
    # Make a prediction using the model
    # Run the inference

    ocr = PaddleOCR(lang='en') # need to run only once to download and load model into memory
    results = ocr.ocr(image, cls=False)

    # Loop through the OCR results and draw bounding boxes and text
    #print(results)
    # return the OCR results
    #return {"results": results}
    bbox = []
    text = []

    for subarray in results:
        for subsubarray in subarray:
            coordinates = subsubarray[0]
            tex_t = subsubarray[1][0]
            number = subsubarray[1][1]
            
            #for result in result:
            # Get the coordinates of the bounding box
            #box = result[0]
            
            # Convert the coordinates to integers
            #box = [int(x) for x in box]
            box = bbox_norm(coordinates)

            bbox.append(box)
            text.append(tex_t)
    
    print(bbox,text) 
    return {"bbox": bbox, "text": text}


