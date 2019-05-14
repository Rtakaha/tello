import tello
from tello_control_ui_aruco import TelloUI
from time import sleep
import threading
import sys
from main_seq import *


drone = False
telloui = False
commands = []
all_detected_ids = set()

class GetSensor:
    def __init__(self, drone):
        self.height = 0
        self.speed = 0
        self.battery = 0
        self.drone = drone

    def get_height(self):
        self.height = self.drone.get_height()
        return self.height*10 # cm

    def get_speed(self):
        self.speed = self.drone.get_speed()
        return self.speed

    def get_battery(self):
        self.battery = self.drone.get_battery()
        return self.battery

def sequence_thread():
    sleep(2)
    print('[seq] Start!')
    gs = GetSensor(drone)
    for command in commands:
        height = gs.get_height()
        speed = gs.get_speed()
        battery = gs.get_battery()
        print("height")
        print(height)
        print("speed")
        print(speed)
        print("battery")
        print(battery)
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

if __name__ == "__main__":
    # launch tello
    drone = tello.Tello('', 8889)
    telloui = TelloUI(drone, "./img/")
    # telloui.marker_detected = marker_detected

    thread = threading.Thread(target=sequence_thread)
    thread.start()

    # run sequencer thread

    # make instances of command classes
    commands.append(Command('takeoff'))
    commands.append(CommandSleep(5))
    commands.append(Command('land'))

	# start the Tkinter mainloop
    telloui.root.mainloop()
