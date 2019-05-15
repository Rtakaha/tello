import tello
from tello_control_ui_aruco import TelloUI
from time import sleep
import threading
import sys
# from get_distance import GetSensor

drone = False
telloui = False
commands = []
all_detected_ids = set()
x = 0
y = 0
z = 0
repair_list = []
zero = 0

class Command:
    def __init__(self, type):
        self.type = type

# Interprets command classes and controls tello
def sequence_thread():
    sleep(2)
    print('[seq] Start!')
    for command in commands:
        if isinstance(command, Command):
            if command.type == 'go2heritage':
                go2heritage()
            elif command.type == 'turn_AR':
                turn_AR()
            elif command.type == 'check_damage':
                check_damage()
            elif command.type == 'back2home':
                back2home()
            else:
                print(command)
    print('[seq] exitting...')
    telloui.onClose()

def marker_detected(ids):
    global all_detected_ids
    global repair_list
    global zero
#    print(ids)
    all_detected_ids |= set(ids)
    for id in all_detected_ids:
        if not id in repair_list:
            if id == 0:
                zero = 1
                print("haha")
            elif not id == 0:
                repair_list.append(id)

    print(repair_list)

def go2heritage():
    global y
    # global z
    print("go to heritage")
    drone.takeoff()
    sleep(10)
    # height = drone.get_height()
    # sleep(7)
    # a = 0.9 - height
    a = 0.3
    drone.move_up(a)
    sleep(7)
    drone.move_backward(4.0)
    print("ok")
    y += 4
    sleep(10)
    # height = drone.get_height()
    # sleep(7)
    # b = height - 0.7
    b = 0.3
    drone.move_down(b)
    # z = height

def turn_AR():
    global zero
    print("turn_AR")
    sleep(2)
    while(1):
        if zero == 1:
            print("ok")
            sleep(10)
            drone.rotate_ccw(180)
            sleep(10)
            break
    # telloui.onClose()

def check_damage():
    print("check damage")
    drone.move_up(0.7)
    sleep(10)
    drone.move_left(0.3)
    sleep(10)
    drone.move_right(0.6)
    sleep(10)
    drone.move_left(0.3)
    sleep(10)
    drone.rotate_cw(180)
    # print("markers: " + str(repair_list))

def back2home():
    print("back to home")
    sleep(5)
    # if x > 0:
    #     drone.move_left(abs(x))
    # elif (x < 0):
    #     drone.move_right(abs(x))
    drone.move_forward(y)
    sleep(5)
    drone.land()
    alert = 0
    serious = 0
    for id in repair_list:
        if id % 2 == 0:
            alert += 1
        elif id % 2 == 1:
            serious += 1

    print("markers: " + str(repair_list))
    print("alert: " + str(alert))
    print("serious: " + str(serious))

if __name__ == "__main__":

    # launch tello
    drone = tello.Tello('', 8889)
    telloui = TelloUI(drone, "./img/")
    telloui.marker_detected = marker_detected

    thread = threading.Thread(target=sequence_thread)
    thread.start()

    # run sequencer thread

    # make instances of command classes
    # commands.append(Command('go2heritage'))
    commands.append(Command('turn_AR'))
    commands.append(Command('check_damage'))
    # commands.append(Command('back2home'))

	# start the Tkinter mainloop
    telloui.root.mainloop()
