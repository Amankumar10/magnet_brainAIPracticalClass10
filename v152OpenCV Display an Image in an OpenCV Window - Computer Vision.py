import cv2 

img = cv2.imread('./data/WhatsApp Image 2024-03-22 at 3.27.36 PM.jpeg')

print(img)

print(type(img))

#Display

cv2.imshow('Our image', img)

#Display for longer duration or To copy keyboard input 
# cv2.waitKey(5)
x=cv2.waitKey(0)
print('Key pressed-->',x)

