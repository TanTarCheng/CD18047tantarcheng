import cv2
import PoseModule as pm


cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmlist = detector.findPosition(img)
    print(lmlist)
    cv2.imshow("Image", img)
    cv2.waitKey(1)