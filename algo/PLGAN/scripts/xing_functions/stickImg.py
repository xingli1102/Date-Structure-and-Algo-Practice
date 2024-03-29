from pdb import set_trace as st
import os
import numpy as np
import cv2
import glob

def get_sorted_files(Directory):
	filenamelist = []
	for root, dirs, files in os.walk(Directory):
		for name in files:
			fullname = os.path.join(root, name)
			filenamelist.append(fullname)
	return sorted(filenamelist)

img_A = []
img_B = []

print("Reading Folder A")
filenames_A = get_sorted_files('/home/xing/maps-20m/Caracas/info_patch_20m/')
filenames_A.sort(key=lambda f: int(filter(str.isdigit, f)))
for img in filenames_A:
	print(img)
	temp = cv2.imread(img)
	temp_resize = cv2.resize(temp, (256, 256))
	img_A.append(temp_resize)

print("Reading Folder B")
filenames_B = get_sorted_files('/home/xing/maps-20m/Caracas/simulation-results/GT/')
filenames_B.sort(key=lambda f: int(filter(str.isdigit, f)))
for img in filenames_B:
	print(img)
	temp = cv2.imread(img)
	temp_resize = cv2.resize(temp, (256, 256))
	img_B.append(temp_resize)

print("Saving Combined")
for i in range (len(img_A)):
	if img_B[i].mean() < 200:
		combinedImg = np.concatenate((img_A[i], img_B[i]), axis=1)
		cv2.imwrite(("/home/xing/pix2pix/datasets/map2simPOS/train/Caracas_"+str(i+1)+".jpg"), combinedImg)



