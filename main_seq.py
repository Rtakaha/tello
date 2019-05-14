import tello
from tello_control_ui_aruco import TelloUI
from time import sleep
import threading
import sys
from get_distance import GetDistance


drone = False
telloui = False
commands = []
all_detected_ids = set()

# Command class
#   represents a command without parameters
class Command:
    def __init__(self, type=None, distance=None, digree=None, clockwise=1):
        self.type = type

# CommandSleep class
class CommandSleep:
    # time(sec)
    def __init__(self, time):
        self.time = time

# Interprets command classes and controls tello
def sequence_thread():
    sleep(2)
    print('[seq] Start!')
    gd = GetDistance(drone)
    for command in commands:
        height = gd.get_height()
        speed = gd.get_speed()
        print("height")
        print(height)
        print("speed")
        print(speed)
        if isinstance(command, Command):
            if command.type == 'takeoff':
                drone.takeoff()
            elif command.type == 'land':
                drone.land()
            else:
                print(command)
        elif isinstance(command, CommandSleep):
            sleep(command.time)
        else:
            print(command)

    print('[seq] exitting...')
    telloui.onClose()

def marker_detected(ids):
    global all_detected_ids
#    print(ids)
    all_detected_ids |= set(ids)
    print(all_detected_ids)

if __name__ == "__main__":
    # launch tello
    drone = tello.Tello('', 8889)
    telloui = TelloUI(drone, "./img/")
    telloui.marker_detected = marker_detected

    thread = threading.Thread(target=sequence_thread)
    thread.start()

    # run sequencer thread

    # make instances of command classes
    commands.append(Command('takeoff'))
    commands.append(CommandSleep(5))
    commands.append(Command('land'))

	# start the Tkinter mainloop
    telloui.root.mainloop()