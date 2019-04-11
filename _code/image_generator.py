from PIL import Image
import os
import requests
from requests.auth import HTTPBasicAuth
import numpy as np
import matplotlib.pyplot as plt
from skimage import io
import glob


#f_name='P1'

out ={}

images = glob.glob('data/*.jpg')
#Load Image
for image in images:
	with open(image,'rb') as file:
		file_name=image.split('/')[1].split('.')[0]
		img=Image.open(file)
		img=img.resize((255,255),Image.ANTIALIAS)
		img.save('output/'+file_name+'.jpg')
		pix_val = list(img.getdata())
		pix_val_2 = [list(elem) for elem in pix_val]
		out[file_name]=pix_val_2
		
