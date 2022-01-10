#Getting required modules
import os
os.system('prompt Hacking: ')
os.system('title Hacking')
os.system('pip install pyautogui')
os.system('pip install opencv-python')
os.system('pip install phonenumbers')
os.system('pip install rotate-screen')
os.system('pip install pywin32')

#importing required modules
import subprocess
import re
import time
from time import sleep
import webbrowser
import random
import cv2
import itertools
import threading
import sys
import pyautogui
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import rotatescreen


RandNo= random.randint(1, 20)#Generating random number

vid = cv2.VideoCapture(0)#Getting video

global user
os.system('cls')

print("Well we are now ready to see a movie")
sleep(1)

#Color changing part
user = os.getlogin()
print("Hello " + user + " . I am a hacker")
os.system('color a')
sleep(0.1)
os.system('color b')
sleep(0.1)
os.system('color c')
sleep(0.1)
os.system('color d')
sleep(0.1)
os.system('color e')
sleep(0.1)
os.system('color f')
sleep(0.1)
os.system('color 0')
sleep(0.1)
os.system('color 1')
sleep(0.1)
os.system('color 2')
sleep(0.1)
os.system('color 3')
sleep(0.1)
os.system('color 4')
sleep(0.1)
os.system('color 5')
sleep(0.1)
os.system('color 6')
sleep(0.1)
os.system('color 7')
sleep(0.1)
os.system('color a')

#Getting wifi passwords
print("I can see all your stored wifi!")
os.system('netsh wlan show profiles')
sleep(1)

print("I am a hacker and can also see all your wifi passwords too")
print("Wait a min!")
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
wifi_list = list()
if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = dict()
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile) 
for x in range(len(wifi_list)):
    print(wifi_list[x]) 
sleep(1)

#Getting drivers
print("Let's see what are the drivers installed in your PC: ")
os.system('driverquery /FO list /v')
os.system('driverquery /FO list /v |clip')
os.system('driverquery > %userprofile%/desktop/driver.txt')

#Killing taskbar
print("Now doing some adult work!!")
sleep(2)
os.system('taskkill /f /im explorer.exe')
print("How do you feel")
sleep(1)
print("If you try to close it now. You will be stuck")

#moving mouse randomly
print("Your mouse won't work any longer")
pyautogui.FAILSAFE = False
while x==RandNo:
    time.sleep(6)
    for i in range(0, 100):
        pyautogui.moveTo(10, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(100, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(200, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(300, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(400, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(500, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(600, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(800, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(900, i * 5)
    for i in range(0, 100):
        pyautogui.moveTo(1000, i * 5)

#Faking animation
done = False
#here is the animation
def animate1():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rGetting stored password from registry. ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!                                              ')

t = threading.Thread(target=animate1)
t.start()
#long process here
time.sleep(5)
done = True

sleep(1)
done = False
def animate2():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rGenerating log file with all data in it ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rSending to host!                                        ')

t = threading.Thread(target=animate2)
t.start()

#long process here
time.sleep(10)
done = True

#Video capturing
sleep(1)
print("Fun Time")
screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation

#Rotating screen
for i in range(1, RandNo):
    pos = abs((start_pos - i*90) % 360)
    screen.rotate_to(pos)
    time.sleep(1.5)

#Phone number info
#setting variables
global PhnNmbrs #Setting "PhnNmbrs" as global var.
PhnNmbrs = input("Enter your phone number with country code: ") #Taking input
PhnNmbr = phonenumbers.parse(PhnNmbrs) #parsing the phone number
print(PhnNmbr)
sleep(2)
#calling Functions
#Getting SIM info
print("\n")
print("SIM:-")
print(carrier.name_for_number(PhnNmbr, 'en'))
print("\n")
#Getting country.
print("Country:-")
print(geocoder.description_for_number(PhnNmbr, 'en'))
print("\n")
#Getting time zone.
print("Time Zone:-")
print(timezone.time_zones_for_number(PhnNmbr))
print("\n")
#Is the phone number valid?
print("Is the phone number valid?")
print(phonenumbers.is_valid_number(PhnNmbr))
print("\n")
#Is the phone number possible?
print("Is the phone number possible?")
print(phonenumbers.is_possible_number(PhnNmbr))
print("\n")

os.system('explorer')