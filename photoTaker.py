import os
import cv2
import time

name='NEW PERSON'     #  YENİ KULLANICI ADI <------ YENİ KULLANICI DATASI OLUŞTURMAK İÇİN 
numOfPhotos=40
vid=cv2.VideoCapture(0)
os.mkdir("data/people/{name}".format(name=name))


def shootPhotos(count):
    for i in range(count):
        ret,frame=vid.read()
        cv2.imwrite("data/people/"+ name + "/{photo}_".format(photo=name)+str(i)+".jpg",frame)  # save the image
        time.sleep(0.1)    
        

while True:                              # WEBCAM AÇILIYOR
    ret,frame=vid.read()
    frame=cv2.flip(frame,1)
    cv2.imshow("Cam",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):  # Q TUŞUNA BASARAK FOTOĞRAFLARI ÇEKMEYE BAŞLA
        shootPhotos(numOfPhotos)         # FOTOĞRAFLARI ÇEKİP KAYDEDEN FONKSİYONA GİT
        break                            # PROGRAMI BİTİR

vid.release()
cv2.destroyAllWindows()







