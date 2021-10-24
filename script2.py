import cv2
import glob

images=glob.glob("*.jpg")
#FOR every image in our images in the folder, read it, resize it to 100*100, show it for 0.5 seconds and save it under the name- RESIZED_***
for image in images:
    name=image.split("_")
    #print(name[0])resized_!
    if name[0]!="resized":#only if we didnt resize it, save it.
        img=cv2.imread(image,0)
        resized=cv2.resize(img,(100,100))
        cv2.imshow(name[0],resized)
        cv2.waitKey(500)#0.5 seconds
        cv2.destroyAllWindows()

        cv2.imwrite("resized_"+image,resized)
