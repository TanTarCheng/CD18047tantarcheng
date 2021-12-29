# import the time module
import time


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(str(t))
        time.sleep(1)
        t -= 1

    print('Fail!!')

# function call
countdown(int(5))

'''countdown = 20
       while countdown:
           mins, secs = divmod(countdown, 60)
           timer = '{:02d}:{:02d}'.format(mins, secs)
           countdown -= 1
           cv2.putText(img, str(countdown), (500, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 0), 5)
           #print('Fail!!')'''