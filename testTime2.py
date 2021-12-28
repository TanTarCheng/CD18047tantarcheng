# import the time module
import time


# define the countdown func.
countdown = 5
while countdown:
    mins, secs = divmod(countdown, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(str(countdown))
    time.sleep(1)
    countdown -= 1
print('Fail!!')


