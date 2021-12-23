import cv2
import numpy as np
import PoseModule as pm
import time

#turn to right hand side  head
cap= cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
totalCount = 20


def calculate_post(img):
    global count
    global totalCount
    global dir
    lmlist = detector.findPosition(img, False)

    if len(lmlist) != 0:
        angle = detector.findAngle(img, 8, 10, 12)
        # range (210 -310) convert to 0 - 100 percent
        per = np.interp(angle, (255, 270), (0, 100))
        # 650= min bar , 100 = max bar opencv is oppesite de
        bar = np.interp(angle, (255, 270), (650, 100))

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
    cv2.putText(img, f'{int(per)}%', (1170, 75), cv2.FONT_HERSHEY_PLAIN, 3, color, 4)

    # Draw count
    #cv2.rectangle(img, (0, 550), (300, 720), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, str(int(count)), (30, 680), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)
    # show the total number
    cv2.putText(img, f'{int(totalCount)} left', (20, 620), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)



def main():
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        img = detector.findPose(img, False)
        calculate_post(img)


        if totalCount == 0.5:
            cv2.putText(img, " Completed!!!", (10, 120), cv2.FONT_HERSHEY_PLAIN, 10, (255, 255, 0), 10)
        if totalCount == 0:
            time.sleep(2)
            break

        cv2.imshow("image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()