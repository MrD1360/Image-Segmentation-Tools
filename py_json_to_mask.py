# import some libraries
import numpy as np
import os
import json
import glob
from skimage import draw
from skimage import io
from tqdm import tqdm
from skimage import img_as_ubyte




# variable definiction
name_folder= 'training_folder'   #to be define each time you run in a different folder
PATH_DIR = ''
ext = '.jpg'  #img extension in which you want to save the masks


os.chdir(name_folder)  #start working in that folder


width,height= 1920,1280 #dimensions of the masks

# create a list of json files
json_list = []

for json_name in glob.glob('*.json'):   
	json_list.append(json_name)


# read each json in the list
for json_name in tqdm(json_list):
	json_path = os.path.join(PATH_DIR, json_name)

	# open a json file
	with open(json_path) as json_file:  
		# load the json
		data = json.load(json_file)

		#go deeper in the structure of the json to find the 
		for el2 in data['_via_img_metadata']:
			print(el2,"file is running")

			#get mask path
			name_new_mask= data['_via_img_metadata'][el2]['filename']
			mask_path = os.path.join(name_new_mask.split('.')[0] + '_temsk' + ext)

			#create matrix for mask
			mask = np.zeros((height, width))

			regions=data['_via_img_metadata'][el2]['regions']

			for reg in regions: #draw the regions
				for shape in reg: #one per time
					if not (shape=='shape_attributes'):
						continue
					# search for points
					points = np.array((reg[shape]['all_points_x'],reg[shape]['all_points_y']), dtype='int32')
					# draw the polygon 
					row_index, col_index = draw.polygon(points[1,:], points[0,:])
					# put ones in the mask
					mask[row_index, col_index] = 1 #or 255
					
			# save the mask
			io.imsave(mask_path, img_as_ubyte(mask))