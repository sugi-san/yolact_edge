import os
import shutil
import cv2

def video_2_images(video_file):                  

    # 既に images フォルダーがあれば削除し、再度images フォルダーを作る
    if os.path.isdir('images'):
         shutil.rmtree('images')
    os.makedirs('images', exist_ok=True)
 
    # Initial setting
    image_dir='./images/'
    image_file='%s.jpg' 
    i = 0
    interval = 1
    length = 18000 # 最大フレーム数
    
    cap = cv2.VideoCapture(video_file)
    while(cap.isOpened()):
        flag, frame = cap.read()  
        if flag == False:  
                break
        if i == length*interval:
                break
        if i % interval == 0:    
           cv2.imwrite(image_dir+image_file % str(int(i/interval)).zfill(6), frame)
        i += 1 
    cap.release()  
