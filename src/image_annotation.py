from __future__ import print_function, division

__author__ = 'amrit'

import sys
from pymongo import MongoClient, InsertOne, DeleteMany, ReplaceOne, UpdateOne
import pymongo
import gridfs
from PIL import Image
import os
import numpy as np
import io
from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/amrit/medicine/google_cloud_key.json"

def dicom2png(byte_data='', shape=[],filename=""):
    z = np.frombuffer(byte_data, dtype=np.uint8)
    x=z.reshape(tuple(shape))
    # Convert to float to avoid overflow or underflow losses.
    image_2d = x.astype(float)
    # Rescaling grey scale between 0-255
    image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    # Convert to uint
    image_2d_scaled = np.uint8(image_2d_scaled)
    # Write the PNG file
    new_im = Image.fromarray(image_2d_scaled)
    path=os.getcwd()+"/png/"+filename+".png"
    new_im.save(path)

def detect_text(byte_data='', shape=[]):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()
    z = np.frombuffer(byte_data, dtype=np.uint8)
    x=z.reshape(tuple(shape))

    # image_2d = x.astype(float)
    # image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max()) * 255.0
    # image_2d_scaled = np.uint8(image_2d_scaled)
    # new_im = Image.fromarray(image_2d_scaled)

    new_im = Image.fromarray(x)

    imgByteArr = io.BytesIO()
    new_im.save(imgByteArr, format='PNG')
    imgByteArr = imgByteArr.getvalue()


    image = vision.types.Image(content=imgByteArr)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                        for vertex in text.bounding_poly.vertices])
    return texts

client = MongoClient(host=['localhost:27017'])
#client=MongoClient("mongodb://Admin:admin@54.191.161.228")
db = client.DICOM
collection=db['dicom_data']
fs = gridfs.GridFS(db)
organs=["spine","cervix","placenta","femur","liver","u. bladder","uterus","u.bladder", "u bladder","ubladder","lt. kidney","lt kidney",
        "lt.kidney","ltkidney","rt. kidney","rt kidney","rt.kidney","rtkidney","lt.lobe","lt. lobe","lt lobe","ltlobe","rt.lobe","rt. lobe","rt lobe","rtlobe",
        "prostate","spleen","rt. ovary","rt ovary","rt.ovary","rtovary","lt. ovary","lt ovary","lt.ovary","ltovary","cbd","c.b.d","gb","g.b"
        ,"FOETAL HEAD","pancreas","r.i.f.region","r.i.f. region","rif region","rifregion","breast","breast1","nipple","foetus"]

for i in fs.find({}):
    #print(i.read())
    #print(i._id)
    #print(tuple(i.shape))
    # byte_data=i.read()
    # shape=i.shape
    #dicom2png(byte_data=i.read(),shape=i.shape,filename='IM_0001')
    response = detect_text(byte_data=i.read(),shape=i.shape)
    response_text = response[0].description
    print(response_text.lower().split("\n"))
