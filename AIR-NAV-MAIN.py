import cv2 as cv
import mediapipe as mp
import time
import htmodule as htm
import math
import keyboard
import numpy as np
from pynput.mouse import Button, Controller



wcam,hcam=640,480
capture = cv.VideoCapture(0)
hand_detector = htm.HandDetector()
mouse = Controller()


screen_width = 1920
screen_height = 1080
rect_height = 355
rect_top = 0


previous_mouse_position = (0, 0)
move_threshold = 10 
last_move_time = 0  
smooth_factor = 0.25


pTime = 0
cTime = 0

last_action_time = 0
cooldown_time = 3

last_action_timeStop = 0
cooldown_timeStop = 3

last_action_timeStopVF = 0
cooldown_timeStopVF = 3

last_action_timeStopWT = 0
cooldown_timeStopWT = 3

last_action_timeStopZoom = 0
cooldown_timeStopZoom = 1

last_action_timeStopZoomOut = 0
cooldown_timeStopZoomOut = 1

left_click_cooldown = 2 
right_click_cooldown = 2  
last_left_click_time = 0 
last_right_click_time = 0 

last_scroll_time = 0
cooldown_scroll_time = 0.25
prev_y1 = None
prev_y2 = None

last_scroll_time_sh = 0
cooldown_scroll_time_sh = 1.5
prev_y1_sh = None

flag=True
volumeFlag=False
while True:
    isTrue,img = capture.read() 
    img_height,img_width = img.shape[:2]
    if not isTrue:
        break

    img,num_hands=hand_detector.findHands(img)

    if num_hands==1:
        hand_list = hand_detector.findPosition(img,num_hands-1)
    elif num_hands==2:
        hand1_list,hand2_list = hand_detector.findPosition(img,num_hands-1)



    if num_hands==1 and len(hand_list)>0:
        x1,x2 = hand_list[3][1],hand_list[4][1]
        y1,y2 = hand_list[6][2],hand_list[8][2]
        y3,y4 = hand_list[10][2],hand_list[12][2]
        y5,y6 = hand_list[14][2],hand_list[16][2]
        y7,y8 = hand_list[19][2],hand_list[20][2]
        count = 0
        thumb,index,middle,ring,last=False,False,False,False,False
        if x1>x2:
            count+=1
            thumb=True
        if y1>y2:
            count+=1
            index=True
        if y3>y4:
            count+=1
            middle=True
        if y5>y6:
            count+=1
            ring=True
        if y7>y8:
            count+=1
            last=True
        

        rect_width = int(img_width * 0.75)
        rect_height = int(img_height * 0.75)
        top_left = ((img_width - rect_width) // 2, (img_height - rect_height) // 2)
        bottom_right = (top_left[0] + rect_width-(rect_width//5), top_left[1] + rect_height-(rect_width//5))
        cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)

        if thumb == False and index == True and middle == False and ring == False and last == False and flag:
            x, y = hand_list[8][1], hand_list[8][2]
            rect_left, rect_top = top_left
            rect_right, rect_bottom = bottom_right
            screen_x = int(np.interp(x, (rect_left, rect_right), (0, screen_width)))
            screen_y = int(np.interp(y, (rect_top, rect_bottom), (0, screen_height)))
            distance = math.hypot(screen_x - previous_mouse_position[0], screen_y - previous_mouse_position[1])
            if distance > move_threshold:
                screen_x = int(previous_mouse_position[0] + (screen_x - previous_mouse_position[0]) * smooth_factor)
                screen_y = int(previous_mouse_position[1] + (screen_y - previous_mouse_position[1]) * smooth_factor)
                mouse.position = (screen_x, screen_y)
                previous_mouse_position = (screen_x, screen_y)
        elif thumb == False and index == True and middle == True and ring == False and last == False and flag:
            current_time = time.time()
            if current_time - last_left_click_time >= left_click_cooldown:
                mouse.click(Button.left, 1) 
                last_left_click_time = current_time  

        elif thumb == False and index == True and middle == True and ring == True and last == False and flag:
            current_time = time.time()
            if current_time - last_right_click_time >= right_click_cooldown:
                mouse.click(Button.right, 1) 
                last_right_click_time = current_time


        if thumb==True and index==True and middle==False and ring==False and last==False and flag:
            x1,y1 = hand_list[4][1],hand_list[4][2]
            x2,y2 = hand_list[8][1],hand_list[8][2]
            c1,c2 = (x1+x2)//2,(y1+y2)//2
            length = math.hypot(x2-x1,y2-y1)
            cv.circle(img,(x1,y1),20,(0,255,0),-1)
            cv.circle(img,(x2,y2),20,(0,255,0),-1)
            if length<80:
                current_time = time.time()
                if current_time - last_scroll_time >= cooldown_scroll_time:  
                    if prev_y1 is not None and prev_y2 is not None:
                        if prev_y1 > y1 and prev_y2 > y2:
                            mouse.scroll(0, 3) 
                        elif prev_y1 < y1 and prev_y2 < y2:
                            mouse.scroll(0, -3)
                    last_scroll_time = current_time
                prev_y1 = y1
                prev_y2 = y2
        
        if thumb==False and index==False and middle==False and ring==False and last==True and flag:
            x1,y1 = hand_list[20][1],hand_list[20][2]
            cv.circle(img,(x1,y1),20,(0,255,0),-1)
            current_time = time.time()
            if current_time - last_scroll_time_sh >= cooldown_scroll_time_sh:  
                if prev_y1_sh is not None:
                    if prev_y1_sh < y1:
                        mouse.scroll(0, -1)
                last_scroll_time_sh = current_time
            prev_y1_sh = y1


        if thumb==False and index==False and middle==False and ring==True and last==False and flag:
            x1,y1 = hand_list[20][1],hand_list[20][2]
            cv.circle(img,(x1,y1),20,(0,255,0),-1)
            current_time = time.time()
            if current_time - last_scroll_time_sh >= cooldown_scroll_time_sh:  
                if prev_y1_sh is not None:
                    if prev_y1_sh < y1:
                            mouse.scroll(0, 1) 
                last_scroll_time_sh = current_time
            prev_y1_sh = y1



        if thumb==True and index==True and middle==False and ring==False and last==False and flag and volumeFlag:
            x1,y1 = hand_list[4][1],hand_list[4][2]
            x2,y2 = hand_list[8][1],hand_list[8][2]
            c1,c2 = (x1+x2)//2,(y1+y2)//2
            length = math.hypot(x2-x1,y2-y1)
            cv.circle(img,(x1,y1),20,(0,255,0),-1)
            cv.circle(img,(x2,y2),20,(0,255,0),-1)
            if 80<length<200:
                cv.circle(img,(c1,c2),20,(255,0,0),-1)
                keyboard.press_and_release('volume down')
            elif length>=200:
                cv.circle(img,(c1,c2),20,(0,0,255),-1)
                keyboard.press_and_release('volume up')
            cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)


        if thumb==True and index==True and middle==True and ring==False and last==False and flag:
            x1,y1 = hand_list[4][1],hand_list[4][2]
            x2,y2 = hand_list[8][1],hand_list[8][2]
            x3,y3 = hand_list[12][1],hand_list[12][2]
            c1,c2 = (x1+x2)//2,(y1+y2)//2
            length = math.hypot(x2-x1,y2-y1)
            lm = math.hypot(x3-x1,y3-y1)
            cv.circle(img,(x1,y1),20,(0,255,0),-1)
            cv.circle(img,(x2,y2),20,(0,255,0),-1)
            cv.circle(img,(x3,y3),20,(0,255,0),-1)
            if time.time()-last_action_time>cooldown_time:
                if 0 <length<=80 and 0<lm<=80:
                    keyboard.press_and_release('windows+print screen')
                    last_action_time=time.time()


        if thumb==False and index==True and middle==True and ring==True and last==True and flag:
            if time.time() - last_action_timeStopWT > cooldown_timeStopWT:
                keyboard.press_and_release('windows+tab')
                last_action_timeStopWT = time.time()


        if thumb==True and index==True and middle==True and ring==True and last==True:
            if time.time() - last_action_timeStop > cooldown_timeStop:
                flag = not flag 
                last_action_timeStop = time.time()
                print(f"Gestures {'paused' if not flag else 'resumed'}")

    if num_hands==2 and len(hand1_list)>0 and len(hand2_list)>0 and flag:
        x1, x2 = hand1_list[3][1], hand1_list[4][1]
        y1, y2 = hand1_list[6][2], hand1_list[8][2]
        y3, y4 = hand1_list[10][2], hand1_list[12][2]
        y5, y6 = hand1_list[14][2], hand1_list[16][2]
        y7, y8 = hand1_list[19][2], hand1_list[20][2]
        xx1 = hand1_list[4][1]
        thumb1, index1, middle1, ring1, last1 = False, False, False, False, False
        count1 = 0
        if x1 < x2:
            count1 += 1
            thumb1 = True
        if y1 > y2:
            count1 += 1
            index1 = True
        if y3 > y4:
            count1 += 1
            middle1 = True
        if y5 > y6:
            count1 += 1
            ring1 = True
        if y7 > y8:
            count1 += 1
            last1 = True

        x1, x2 = hand2_list[3][1], hand2_list[4][1]
        y1, y2 = hand2_list[6][2], hand2_list[8][2]
        y3, y4 = hand2_list[10][2], hand2_list[12][2]
        y5, y6 = hand2_list[14][2], hand2_list[16][2]
        y7, y8 = hand2_list[19][2], hand2_list[20][2]
        thumb2, index2, middle2, ring2, last2 = False, False, False, False, False
        xx2 = hand2_list[4][1]
        count2 = 0
        if x1 > x2:
            count2 += 1
            thumb2 = True
        if y1 > y2:
            count2 += 1
            index2 = True
        if y3 > y4:
            count2 += 1
            middle2 = True
        if y5 > y6:
            count2 += 1
            ring2 = True
        if y7 > y8:
            count2 += 1
            last2 = True

        if xx1>xx2:
            break

        if index1 and index2 and not thumb1 and not middle1 and not ring1 and not last1 and not thumb2 and not middle2 and not ring2 and not last2:
            if time.time() - last_action_timeStopVF > cooldown_timeStopVF:
                print("Volume Switch")
                volumeFlag=not volumeFlag
                last_action_timeStopVF = time.time()
        

        if index1 and index2 and middle1 and middle2 and ring1 and ring2:
            print("yes")
            if time.time() - last_action_timeStopZoomOut > cooldown_timeStopZoomOut:
                keyboard.press_and_release('ctrl+-')
                last_action_timeStopZoomOut = time.time()
        elif index1 and index2 and middle1 and middle2 and not thumb1 and not ring1 and not last1 and not thumb2 and not ring2 and not last2:
            if time.time() - last_action_timeStopZoom > cooldown_timeStopZoom:
                keyboard.press_and_release('ctrl+shift+=')
                last_action_timeStopZoom = time.time()

        
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv.putText(img,"FPS: "+str(int(fps)),(30,30),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
    img = cv.resize(img, (wcam, hcam), interpolation=cv.INTER_AREA)
    cv.imshow('Video',img)
    if (cv.waitKey(1) & 0XFF)==ord('q'):
        break
