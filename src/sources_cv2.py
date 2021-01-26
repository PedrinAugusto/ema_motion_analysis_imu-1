import cv2
import numpy as np
import pandas as pd
import math



def defineStartEnd(video_path, n_frames, frame_no=0):
    cap = cv2.VideoCapture(video_path)
    start_end = [0,0]
    moment = 0
    if(cap.isOpened() == False):
        print("Error opening video stream or file")
        print(video_path)
        sys.exit(-1)
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret_val, img = cap.read()
        if ret_val:
            img = cv2.resize(img, (960, 540)) 
            cv2.imshow('Video Analysis', img)
        arg = cv2.waitKey(1)
        if arg == 27:
            break  # esc to quit
        elif arg == 13: # pressed enter
            start_end[moment] = frame_no
            moment = (moment+1)%5
            print(start_end)
        elif arg == 100:
            frame_no = (frame_no+1)%n_frames
        elif arg == 97:
            frame_no = (frame_no-1)%n_frames
    cap.release()
    cv2.destroyAllWindows()
    return start_end


def count_frames(path):

    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        print ("could not open :", path)
    # inicializar os vídeo 
    video = cv2.VideoCapture(path)
    
    # buscar número de frames e frame por segundo
    n_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    #width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    #height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    video.release()
    
    return n_frames, fps #, width, height