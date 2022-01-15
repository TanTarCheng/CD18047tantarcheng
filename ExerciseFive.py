import cv2
import cv2.cv2
import numpy as np
import PoseModule as pm
import time
from datetime import datetime
from threading import Thread
import ExerciseSix as E6

#up &down head
cap= cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
totalCount = 6
diff = 0
exercise_complete = False

def countdown():
    global diff
    duration = 50
    start_time = datetime.now()
    diff = (datetime.now() - start_time).seconds  # converting into seconds
    while (diff <= duration) and (not exercise_complete):
        diff = (datetime.now() - start_time).seconds
        #print(str(diff))
        if diff >= 50:
            break

def onSuccessExercise():
    #get next Exercise reference/ direct import direct
    E6.runExercise()

def set_totalCount(difficulty):
    global totalCount
    totalCount = difficulty


def calculate_post(img):
    global count
    global totalCount
    global dir
    lmlist = detector.findPosition(img, False)

    if len(lmlist) != 0:
        angle = detector.findAngle(img, 11, 0, 12)
        # range (210 -310) convert to 0 - 100 percent
        per = np.interp(angle, (91, 95), (0, 100))
        # 650= min bar , 100 = max bar opencv is oppesite de
        bar = np.interp(angle, (91, 95), (650, 100))

        # check for the curls
        color = (255, 50, 0)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                totalCount -= 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                totalCount -= 0.5
                dir = 0
        display_data(img, color, per, bar)


def display_data(img, color, per, bar):

    # Draw bar
    cv2.rectangle(img, (1190, 100), (1178, 650), color, 3)
    cv2.rectangle(img, (1190, int(bar)), (1178, 650), color, cv2.FILLED)
    cv2.putText(img, f'{int(per)}%', (1150, 75), cv2.FONT_HERSHEY_PLAIN, 3, color, 4)

    # Draw count
    #cv2.rectangle(img, (0, 550), (300, 720), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{str(int(count))} Repitition', (26, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
    # show the total number
    cv2.putText(img, f'{int(totalCount)} left', (26, 620), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

    #display timer text
    cv2.putText(img, (f"{diff}/50sec"), (26, 560), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 4, cv2.LINE_AA)

def main():

    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        img = cv2.flip(img, 1)
        img = detector.findPose(img, False)
        calculate_post(img)

        global exercise_complete
        # each time count 1
        if totalCount == 0.5:
            cv2.putText(img, f'Completed in {diff} second', (360, 220), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
        if totalCount == 0:
            exercise_complete = True
            time.sleep(1)
            onSuccessExercise()

        if diff == 49:
            cv2.putText(img, "Time up, u fail !!!", (360, 220), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 0), 5)
        if diff == 50:
            time.sleep(1)
            break

        #ExercisePicture
        imgPic = cv2.imread('ExercisePic/num9PosteriorScaleneStretch.jpg', -1)
        #ExerciseName
        cv2.putText(img, f'PosteriorScaleneh', (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        cv2.putText(img, f'Stretch', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        #mergeImage
        added_image = cv2.addWeighted(img[150:250, 150:250, :], 0.2, imgPic[0:100, 0:100, :], 1 - 0.4, 0)
        img[150:250, 150:250] = added_image
        cv2.imshow('PosteriorScaleneStretch', img)


        k = cv2.waitKey(1)
        if k & 0xFF == ord("q"):  # quit all
            break

#run from main menu
def runExercise():
    t1 = Thread(target=countdown)
    t2 = Thread(target=main)
    t1.start()  # Calls first function
    t2.start()  # Calls second function to run at same time

#testmodule if u dont run at main menu
if __name__ == "__main__":
    runExercise()
