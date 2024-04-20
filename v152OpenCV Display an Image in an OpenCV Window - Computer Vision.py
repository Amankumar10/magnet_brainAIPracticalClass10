import cv2 

img = cv2.imread('./data/WhatsApp Image 2024-03-22 at 3.27.36 PM.jpeg')

print(img)

print(type(img))

#Display

cv2.imshow('Our image', img)
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
img= cv2.imread('./data/Screenshot from 2024-04-20 16-35-03.png',0)
cv2.imshow('Our image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.destroyAllWindows('./data/Screenshot from 2024-04-20 16-35-03.png')