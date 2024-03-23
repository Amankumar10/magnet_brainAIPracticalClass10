# OpenCV- Introduction
# Opencv is a huge open-source library for computer vision, machine learning, and image processing.
# Now, it plays a major role in real-time operation which is very important in today’s systems. By using it, 
# one can process images and videos to identify objects, faces, or even the handwriting of a human.








import cv2
#syntax 
#img = cv2.imread(path,flag)
img = cv2.imread('WhatsApp Image 2024-03-22 at 3.27.36 PM.jpeg')
print(img)



# Flag
# 1-->cv2.IMREAD_COLOR
# 0 -->cv2.IMREAD_GRAYSCALE
# -1 -->cv2.IMREAD_UNCHANGED
img = cv2.imread('./data/WhatsApp Image 2024-03-22 at 3.27.36 PM.jpeg',0)
print(img)



img = cv2.imread('./data/WhatsApp Image 2024-03-22 at 3.27.36 PM.jpeg',1)
print(img)


img2 = cv2.imread('./data/WhatsApp Image 2024-03-22 at 3.27.36 PM.jpeg',-1)
# print(img2)
# print(type(img2))
print(img2[:,:,0])
# print(img2[0])
print(len(img2[0]))  # width
print(len(img2[:,:,0]))   # height