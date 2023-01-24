import cv2
import numpy as np

import tools

img = cv2.imread("sten/data/supreme_victory.jpeg", cv2.IMREAD_COLOR)

#cv2.imshow("im-lolz", img)
#cv2.waitKey(500)
#print(img[10,10])
#print(tools.StB('salut'))
seq = tools.StB('salut')
#print(seq)

print("\nNew printing")
message = "Toutes vos bases sont nous appartiennent !"
test = tools.imprint(message, img)
diff = tools.difference(img, test)
cv2.imwrite('sten/data/test.jpeg',test )