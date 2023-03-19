# import keyboard
import math
import os
import time
import winsound
from threading import Thread
from pynput import keyboard
from threading import Thread
from os import system
system("title " + os.path.basename(__file__)[0:-3])

# By GokaGokai/ JohnTitorTitor/ Kanon

print("----------------------------------------")
print("\n   " + os.path.basename(__file__)[0:-3])
print(" By GokaGokai/ JohnTitorTitor/ Kanon\n")
print("----------------------------------------")
print("")
print("Press z or x to start")
print("When Retrying or Switching Modes, you have 3 seconds to prepare for the next BPM Cycle")
print("")
print("Shortcuts:")
print("ctrl+alt+a' : Retry BPM and Reset Clicks")
print("ctrl+alt+s' : Retry BPM")
print("ctrl+alt+d' : Reset Clicks")
print("ctrl+alt+f' : Toggle Metronome Mode (For measuring BPM, just tap to the beat)")
print("")



        # 'z': on_activate_z,
        # 'x': on_activate_x,
        # '<ctrl>+<alt>+a' : both,
        # '<ctrl>+<alt>+s' : retryBPM,
        # '<ctrl>+<alt>+d' : resetClicks,
        # '<ctrl>+<alt>+f' : toggleMetronome}) as h:

totalClicks = 0
totalClicksSaved = 0
begin = False
stop = False
sleeping = False
savedBPM = 0
elapsed_time = 0
start_time = 0
metronome = False

def timer():
    global totalClicks
    global totalClicksSaved
    global start_time
    start_time = time.time()
    
    while True:
        global elapsed_time
        elapsed_time = time.time() - start_time
        
        if elapsed_time != 0 :
            beatPerSecond = totalClicks / elapsed_time
            bpm = beatPerSecond * 60 / 4
            # global sleeping
            # if not sleeping :
            global savedBPM
            savedBPM = bpm

            if metronome:
                print(f"BPM: {bpm:.1f} ({elapsed_time:.1f}/40) | Metronome Mode              ", end="\r")
            else:
                print(f"BPM: {bpm:.1f} ({elapsed_time:.1f}/10) | {totalClicksSaved} clicks       ", end="\r")
                
            # sleeping = True
            if metronome:
                time.sleep(1)
            else:
                time.sleep(0.1)
            # sleeping = False

        
        # restart every 10
        if metronome:
            if elapsed_time > 40 :
                totalClicks = 0
                elapsed_time = 0
                start_time = time.time()
        else:
            if elapsed_time > 10 :
                totalClicks = 0
                elapsed_time = 0
                start_time = time.time()

def timerStart():
    global begin
    if not begin:
        thread = Thread(target=timer)
        thread.start()
        begin = True
        print("--------- Started ------------                                   \n")

# def truncate(n, decimals=0):
#     multiplier = 10 ** decimals
#     return int(n * multiplier) / multiplier

# def round_to_10(num):
#     return round(num / 10) * 10

# def round_to_5(num):
#     return round(num / 5) * 5

# from pynput import keyboard
def play_sound():
    winsound.PlaySound("normal-hitnormal", winsound.SND_ALIAS|winsound.SND_ASYNC)

def on_activate_z():
    timerStart()
    print('z pressed                              ')
    play_sound()

    global totalClicks
    global totalClicksSaved
    global metronome

    if metronome: 
        totalClicks += 4
    else:
        totalClicks += 1
        totalClicksSaved += 1


    if metronome:
        print(f"BPM: {savedBPM:.1f} ({elapsed_time:.1f}/40) | Metronome Mode              ", end="\r")
    else:
        print(f"BPM: {savedBPM:.1f} ({elapsed_time:.1f}/10) | {totalClicksSaved} clicks       ", end="\r")

def on_activate_x():
    timerStart()
    print('x pressed                               ')
    play_sound()

    global totalClicks
    global totalClicksSaved
    global metronome
    
    if metronome: 
        totalClicks += 4
    else:
        totalClicks += 1
        totalClicksSaved += 1
    

    if metronome:
        print(f"BPM: {savedBPM:.1f} ({elapsed_time:.1f}/40) | Metronome Mode              ", end="\r")
    else:
        print(f"BPM: {savedBPM:.1f} ({elapsed_time:.1f}/10) | {totalClicksSaved} clicks       ", end="\r")

def resetClicks():
    global totalClicksSaved
    totalClicksSaved = 0
    print('Reset Clicks                          ')

# You have 3 seconds to prepare for the next BPM cycle
def retryBPM():
    global elapsed_time
    global start_time
    global metronome
    global savedBPM
    savedBPM = 0

    if metronome:
        elapsed_time = 37
        start_time = time.time() - 37
    else:
        elapsed_time = 7.0
        start_time = time.time() - 7.0
    print('Retry BPM                              ')

def both():
    global totalClicksSaved
    global elapsed_time
    global start_time
    global metronome
    global savedBPM
    savedBPM = 0
    totalClicksSaved = 0
    
    if metronome:
        elapsed_time = 37
        start_time = time.time() - 37
    else:
        elapsed_time = 7.0
        start_time = time.time() - 7.0
    print('Reset and Retry                                ')

# You have 3 seconds to prepare for Metronome Mode or Normal Mode
def toggleMetronome():
    global elapsed_time
    global start_time
    global metronome
    global savedBPM
    savedBPM = 0

    if metronome:
        elapsed_time = 7
        start_time = time.time() - 7
        metronome = False
        print('Metronome Off                              ')
    elif not metronome:
        elapsed_time = 37
        start_time = time.time() - 37
        metronome = True
        print('Metronome On                               ')
    

with keyboard.GlobalHotKeys({
        'z': on_activate_z,
        'x': on_activate_x,
        '<ctrl>+<alt>+a' : both,
        '<ctrl>+<alt>+s' : retryBPM,
        '<ctrl>+<alt>+d' : resetClicks,
        '<ctrl>+<alt>+f' : toggleMetronome}) as h:
    h.join()
