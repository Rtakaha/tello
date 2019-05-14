import tello
from tello_control_ui_aruco import TelloUI
from time import sleep
import threading
import sys
from get_distance import GetSensor

drone = False
telloui = False
commands = []
all_detected_ids = set()
x = 0
y = 0
z = 0

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
#    print(ids)
    all_detected_ids |= set(ids)
    print(all_detected_ids)

def go2heritage():
    print("go to heritage")
    drone.takeoff()
    sleep(7)
    height = drone.get_height()
    a = 0.9 - height
    drone.move_up(a)
    drone.get_height()
    sleep()
    drone.move_backward(0.5)
    drone.get_height()
    y += 0.5
    sleep(7)
    height = drone.get_height()
    b = height - 0.7
    drone.move_down(b)
    height = drone.get_height()
    z = height
    drone.land()

def turn_AR():
    print("turn_AR")


def check_damage():
    print("check damage")


def back2home():
    print("back to home")


if __name__ == "__main__":
    # launch tello
    drone = tello.Tello('', 8889)
    telloui = TelloUI(drone, "./img/")
    telloui.marker_detected = marker_detected

    thread = threading.Thread(target=sequence_thread)
    thread.start()

    # run sequencer thread

    # make instances of command classes
    commands.append(Command('go2heritage'))
    commands.append(Command('turn_AR'))
    commands.append(Command('check_damage'))
    commands.append(Command('back2home'))

	# start the Tkinter mainloop
    telloui.root.mainloop()
