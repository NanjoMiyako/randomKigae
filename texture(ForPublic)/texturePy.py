import numpy as np
import matplotlib.pyplot as plt
import random


import cv2
import sys

#マスク元画像
#img = cv2.imread("fuku4.bmp",0)

#wearInfo.csvに各服の素材、形状データの組をセット
def selectWearTextureAndMask():
	with open("C:\\HogeHoge\\texture\\wearInfo.csv", mode='r', encoding='utf-8') as f:
		lineList = f.readlines()
		tops = []
		bottoms = []
		shoes = []
		
		
		print(lineList)
		for line1 in lineList:
			tempList = line1.split(",");
			print(tempList)
			if tempList[3] == "トップス\n":
				tops.append(line1)
			elif tempList[3] == "ボトムス\n":
				bottoms.append(line1)
			elif tempList[3] == "シューズ\n":
				shoes.append(line1)
		
		#トップス
		rIdx = random.randint(0, len(tops)-1);
		list1 = tops[rIdx].split(",");
		topsShapeImg = list1[1]
		topsTextureImg = list1[2]
		
		#ボトムス
		rIdx = random.randint(0, len(bottoms)-1);
		list1 = bottoms[rIdx].split(",");
		bottomsShapeImg = list1[1]
		bottomsTextureImg = list1[2]
		
		#シューズ
		rIdx = random.randint(0, len(shoes)-1);
		list1 = shoes[rIdx].split(",");
		shoesShapeImg = list1[1]
		shoesTextureImg = list1[2]
		
		return topsShapeImg, topsTextureImg, bottomsShapeImg, bottomsTextureImg, shoesShapeImg, shoesTextureImg
	
topsShapeImg, topsTextureImg, bottomsShapeImg, bottomsTextureImg, shoesShapeImg, shoesTextureImg = selectWearTextureAndMask()

#テクスチャ画像
img2_1 = cv2.imread(topsTextureImg,1)
img2_2 = cv2.imread(bottomsTextureImg,1)
img2_3 = cv2.imread(shoesTextureImg,1)

img2_1 = cv2.resize(img2_1, (20, 20));
img2_2 = cv2.resize(img2_2, (20, 20));
img2_3 = cv2.resize(img2_3, (20, 20));

#imgはimg2の縦横共に3倍の大きさ
width, height = 60, 60
img3_1 = np.tile(img2_1, (3, 3, 1))
img3_1 = cv2.resize(img3_1,(width, height));

img3_2 = np.tile(img2_2, (3, 3, 1))
img3_2 = cv2.resize(img3_2,(width, height));

img3_3 = np.tile(img2_3, (3, 3, 1))
img3_3 = cv2.resize(img3_3,(width, height));


#白黒反転
#img4 = cv2.bitwise_not(img);

#マスク元画像
img4_1 = cv2.imread(topsShapeImg,0)
img4_1 = cv2.resize(img4_1, (width, height))

img4_2 = cv2.imread(bottomsShapeImg, 0)
img4_2 = cv2.resize(img4_2, (width, height))

img4_3 = cv2.imread(shoesShapeImg, 0)
img4_3 = cv2.resize(img4_3, (width, height))



#出力画像用
img5_1 = cv2.imread("white.jpg", 1)
img5_1 = cv2.resize(img5_1,(width, height))

img5_2 = cv2.imread("white.jpg", 1)
img5_2 = cv2.resize(img5_2,(width, height))

img5_3 = cv2.imread("white.jpg", 1)
img5_3 = cv2.resize(img5_3,(width, height));


startY_1 = 0
endY_1 = 0

startY_2 = 0
endY_2 = 0

startY_3 = 0
endY_3 = 0


#マスク処理1
for i in range(60):
	for j in range(60):
		val1 = img4_1[i,j]
		if val1 != 255:
			img5_1[i,j] = img3_1[i,j]
			
			if startY_1 == 0:
				startY_1 = i
			if endY_1 < i:
				endY_1 = i;
				

img5_1 = img5_1[startY_1:endY_1, 0:60]

cv2.imwrite("out4.jpg",img5_1)

#マスク処理2
for i in range(60):
	for j in range(60):
		val2 = img4_2[i,j]
		if val2 != 255:
			img5_2[i,j] = img3_2[i,j]
			
			if startY_2 == 0:
				startY_2 = i
			if endY_2 < i:
				endY_2 = i;

img5_2 = img5_2[startY_2:endY_2, 0:60]
				
#マスク処理3
for i in range(60):
	for j in range(60):
		val3 = img4_3[i,j]
		if val3 != 255:
			img5_3[i,j] = img3_3[i,j]
			
			if startY_3 == 0:
				startY_3 = i
			if endY_3 < i:
				endY_3 = i;

img5_3 = img5_3[startY_3:endY_3, 0:60]

cv2.imwrite("out5.jpg", img5_2)

img_out = cv2.vconcat([img5_1, img5_2, img5_3]);

cv2.imwrite("out6.jpg", img_out);

