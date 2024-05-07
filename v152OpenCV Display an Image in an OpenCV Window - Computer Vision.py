import cv2 

img = cv2.imread('./data/WhatsApp Image 2024-03-22 at 3.27.36 PM.jpeg')

# print(img)

# print(type(img))

#Display

# cv2.imshow('Our image', img)
# var =cv2.imshow('Our image', img)
# print(var)

#Wait for key press to close window
# cv2.waitKey(0)
#Display for longer duration or To copy keyboard input 
# cv2.waitKey(5)
# x=cv2.waitKey(0)
# print('Key pressed-->',x)


# Destroy
# cv2.destroyAllWindows()


#Different flags
# img= cv2.imread('./data/Screenshot from 2024-04-20 16-35-03.png',0)
# cv2.imshow('Our image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.destroyAllWindows('./data/Screenshot from 2024-04-20 16-35-03.png')


#Different slicing 
# img= cv2.imread('./data/Screenshot from 2024-04-20 16-35-03.png')
# img_modified = img[0:200,:]
# cv2.imshow('Our image',img_modified)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#multiple imshow functions
# img= cv2.imread('./data/Screenshot from 2024-04-20 16-35-03.png')

# cv2.imshow('Our image 1',img)
# cv2.imshow('Our image 2',img)
# cv2.imshow('Our image 3',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




# #display ndarry
# import numpy as np

# # Black Image
# matrx = np.zeros((500,500),dtype='uint8')
# cv2.imshow('Blue Image',matrx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





#display ndarry
import numpy as np
import random
# Black Image
matrx = np.zeros((800,800,3),dtype='uint8')
for i in range(800):
    for j in range(800):
        matrx[i][j]=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        
cv2.imshow('Random Image',matrx)
cv2.waitKey(0)
cv2.destroyAllWindows()