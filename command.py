import Tkinter as tki
from Tkinter import Toplevel, Scale
import datetime
import cv2
import os
import time
import platform
import tello_control_ui_aruco

class FirstCommand:
    def __init__(self, type, distance_for=0, distance_back=0, distance_up=0, distance_down=0, time=5, degree_cw=0):
        self.type = type
        self.distance_for = distance_for
        self.distance_back = distance_back
        self.distance_up = distance_up
        self.distance_down = distance_down
        self.degree_cw = degree_cw
        self.time = time



# class Command:
#     def __init__(self, type, time):
#         self.type = type
#         self.time = time
#
# class CommandMove:
#     def __init__(self, type, distance, time):
#         self.type = type
#         self.distance = distance
#         self.time = time
#
# class CommandUpDown:
#     def __init__(self, type, distance, time):
#         self.type = type
#         self.distance = distance
#         self.time = time
#
# class CommandRotate:
#     def __init__(self, type, degree, time):
#         self.type = type
#         self.degree = degree
#         self.time = time
#
# class CommandSide:
#     def __init__(self, type, distance, time):
#         self.type = type
#         self.degree = distance
#         self.time = time

# CommandSleep class
# class CommandSleep:
#     # time(sec)
#     def __init__(self, time):
#         self.time = time
