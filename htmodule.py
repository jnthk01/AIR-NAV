import cv2 as cv
import mediapipe as mp
import time

class HandDetector:
    def __init__(self,mode=False,max_num_hands=2,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.mode=mode
        self.max_num_hands=max_num_hands
        self.min_detection_confidence=min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, 
                            max_num_hands=self.max_num_hands, 
                            min_detection_confidence=self.min_detection_confidence,
                            min_tracking_confidence=self.min_tracking_confidence) 

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        num_hands = 0

        if self.results.multi_hand_landmarks:
            num_hands = len(self.results.multi_hand_landmarks)
            for handlandmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlandmarks, self.mpHands.HAND_CONNECTIONS)

        return img, num_hands


    def findPosition(self, img, handNo=0):
        self.land_marks = []
        
        if self.results.multi_hand_landmarks:
            if handNo == 0:
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(w * lm.x), int(h * lm.y)
                    self.land_marks.append([id, cx, cy]) 
                return self.land_marks
            elif handNo == 1:
                hand0_landmarks = []
                hand1_landmarks = []
                for hand_index in range(min(2, len(self.results.multi_hand_landmarks))):
                    myHand = self.results.multi_hand_landmarks[hand_index]
                    hand_landmarks = []
                    for id, lm in enumerate(myHand.landmark):
                        h, w, c = img.shape
                        cx, cy = int(w * lm.x), int(h * lm.y)
                        hand_landmarks.append([id, cx, cy])
                    if hand_index == 0:
                        hand0_landmarks = hand_landmarks
                    elif hand_index == 1:
                        hand1_landmarks = hand_landmarks
                return hand0_landmarks, hand1_landmarks



def main():
    capture = cv.VideoCapture(0) 
    pTime = 0
    cTime = 0

    detector = HandDetector()

    while True:
        isTrue,img = capture.read()
        if not isTrue:
            break

        img = detector.findHands(img)
        lm_list = detector.findPosition(img)
        if len(lm_list)!=0:
            print(lm_list[8])

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime=cTime
        cv.putText(img,"FPS: "+str(int(fps)),(30,30),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)

        cv.imshow("Video",img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        cv.waitKey(1)


if __name__=="__main__":
    main()