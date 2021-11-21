from djitellopy import Tello
import cv2
import time

width = 320
height = 240
startCounter = 0

me = Tello()
me.connect()

me.for_back_velocity = 0
me.for_right_velocity = 0
me.up_down_velocity = 0
me.speed = 0
me.yaw_velocity = 0

print(me.get_battery())

if startCounter == 0:
    me.takeoff()
    me.get_height()
    me.move_forward(20)
    me.move_back(40)
    me.land()
