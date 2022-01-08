import cv2
import cv2.cv2
import numpy as np
import PoseModule as pm
import time
from datetime import datetime
from threading import Thread
import ExerciseTwo as E2

#camera capture
cap= cv2.VideoCapture(0)
#posemodule item
detector = pm.poseDetector()
#variable
count = 0
dir = 0
totalCount = 6
diff = 0
exercise_complete = False

#challenge countdown
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

#get next Exercise reference/ go to next exercise
def onSuccessExercise():
    E2.runExercise()

#get total count from main menu
def set_totalCount(difficulty):
    global totalCount
    totalCount = difficulty

#calculate each action player do
def calculate_post(img):
    global count
    global totalCount
    global dir

    lmlist = detector.findPosition(img, False)

    if len(lmlist) != 0:
        angle = detector.findAngle(img, 14, 0, 13)
        # range (210 -310) convert to 0 - 100 percent
        per = np.interp(angle, (240, 250), (0, 100))
        # 650= min bar , 100 = max bar opencv is oppesite de
        bar = np.interp(angle, (240, 250), (650, 100))

        # check for the curls
        color = (255, 50, 0)
        #percent bar reach 100
        if per == 100:
            color = (0, 255, 0)
            #count direction
            if dir == 0:
                count += 0.5
                totalCount -= 0.5
                dir = 1
        #percent bar reach 0
        if per == 0:
            color = (0, 255, 0)
            # count direction
            if dir == 1:
                count += 0.5
                totalCount -= 0.5
                dir = 0
        display_data(img, color, per, bar)

#display the information
def display_data(img, color, per, bar):
    #draw bar and inside bar flow
    cv2.rectangle(img, (1190, 100), (1178, 650), color, 3)
    cv2.rectangle(img, (1190, int(bar)), (1178, 650), color, cv2.FILLED)
    #show percentage
    cv2.putText(img, f'{int(per)}%', (1150, 75), cv2.FONT_HERSHEY_PLAIN, 3, color, 4)

    # show how many repit
    cv2.putText(img, f'{str(int(count))} Repitition', (26, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
    # show the total count number
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

        #set end condition if total count below 1
        if totalCount == 0.5:
            #print complete
            cv2.putText(img, f'Completed in {diff} second', (360, 220), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 0), 5)
        if totalCount == 0:
            #check run complete or not
            exercise_complete = True
            #wait 1 sec
            time.sleep(1)
            #run next exercise
            onSuccessExercise()

        # lose condition
        if diff == 49:
            cv2.putText(img, "Time up, u fail !!!", (360, 220), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 0), 5)
        if diff == 50:
            time.sleep(1)
            #direct break the game
            break

        #show Exercise Picture
        imgPic = cv2.imread('ExercisePic/1CervicalSpineLateralFlexion.jpg', -1)
        #show ExerciseName
        cv2.putText(img, f'CervicalSpine', (10, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        cv2.putText(img, f'LateralFlexion', (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        #merge exercise picture and camare into 1 Image
        added_image = cv2.addWeighted(img[150:250, 150:250, :], 0.2, imgPic[0:100, 0:100, :], 1 - 0.4, 0)
        img[150:250, 150:250] = added_image
        #naming the window as CervicalSpineLateralFlexion
        cv2.imshow('CervicalSpineLateralFlexion', img)

        #set break key  = q
        k = cv2.waitKey(1)
        if k & 0xFF == ord("q"):  # quit all
            break

#run from main menu using this code
def runExercise():
    t1 = Thread(target=countdown)
    t2 = Thread(target=main)
    t1.start()  # Calls first function
    t2.start()  # Calls second function to run at same time
    print('hello wlc Exercise1')

# direct run exersice
if __name__ == "__main__":
    runExercise()
