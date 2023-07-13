#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Thu Jul 13 11:51:37 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'PsychoPy-Practice-Task'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/raphaelgabiazon/Desktop/Practice_Memory-Task/PsychoPy-Practice-Task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1470, 956], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "setUp" ---
# Run 'Begin Experiment' code from setUpCode
import random

# Initialize variables
volume_counter = 1
volume_total = 138 # (10.0 sec x 3) + (6.0 sec x 12) + (3.0 sec x 12)

start_time = 0
current_time = 0

# Create clocks to keep track of the time
timer = core.Clock()

# Create a global clock 
Time_Since_Run = core.Clock()

cross_time = 6.0 # Fixation cross duration
image_time = 3.0 # Stimulus duration
key_board_time = 3.0 # Keyboard response duration during trial

Block_1_Run = 1

# Create counters 
block_loop_trials_counter = 0 # counter for trials in block loops
encode_trials_counter = 0 # counter for encode trials
recognition_trials_counter = 0 # counter for recognition trials
Block_Loop_Voulme_Counter = [] # To reset volume counter

# Initialize the current encoding, recognition, and jitter indices for tracking the current image position and jitter time
current_encode_index = 0
current_recog_index = 0
current_jitter_index = 0

# Initialize the current encoding key index for tracking the list condition in Encoding_Dictionary_Block_1_Run_1
current_encode_key_index = 0

# Set flags for instruction display based on block and condition
Block_1_Run_1_Started = True # Assuming Block 1 Run 1 is first
Block_2_Run_2_Started = False # DELETE?
Block_3_Run_3_Started = False # DELETE?
Fix_Cross_Started = False # Becomes true after first stimulus 
Encoding_Started = True # Encoding condition always first
Recognition_Started = False

# --- Initialize components for Routine "condLoader" ---
# Run 'Begin Experiment' code from condLoaderCode
import pandas as pd
import random 

#BLOCK 1 RUN 1
# Load encoding and recognition conditions and store in dataframe (df)
Block_1_Run_1_Conditions_file = 'conditions.xlsx'
Block_1_Run_1_Conditions_df = pd.read_excel(Block_1_Run_1_Conditions_file)

# Load encoding conditions
Face_Encoding_Block_1_Run_1_file = Block_1_Run_1_Conditions_df.loc[0, 'cond_file']
Place_Encoding_Block_1_Run_1_file  = Block_1_Run_1_Conditions_df.loc[1, 'cond_file']
Pair_Encoding_Block_1_Run_1_file= Block_1_Run_1_Conditions_df.loc[2, 'cond_file']

# Load recognition conditions
Face_Recog_Block_1_Run_1_file = Block_1_Run_1_Conditions_df.loc[3, 'cond_file']
Place_Recog_Block_1_Run_1_file = Block_1_Run_1_Conditions_df.loc[4, 'cond_file']
Pair_Recog_Block_1_Run_1_file = Block_1_Run_1_Conditions_df.loc[5, 'cond_file']

# Store encoding conditions in dataframe (df)
Face_Encoding_Stimuli_Block_1_Run_1_df = pd.read_excel(Face_Encoding_Block_1_Run_1_file)
Place_Encoding_Stimuli_Block_1_Run_1_df = pd.read_excel(Place_Encoding_Block_1_Run_1_file)
Pair_Encoding_Stimuli_Block_1_Run_1_df = pd.read_excel(Pair_Encoding_Block_1_Run_1_file)

# Store recognition conditions in dataframe (df)
Face_Recog_Stimuli_Block_1_Run_1_df = pd.read_excel(Face_Recog_Block_1_Run_1_file)
Place_Recog_Stimuli_Block_1_Run_1_df = pd.read_excel(Place_Recog_Block_1_Run_1_file)
Pair_Recog_Stimuli_Block_1_Run_1_df = pd.read_excel(Pair_Recog_Block_1_Run_1_file)

# Create encoding list of images conditions
Face_Encoding_Images_Block_1_Run_1 = Face_Encoding_Stimuli_Block_1_Run_1_df["encoding_stims"].tolist()
Place_Encoding_Images_Block_1_Run_1 = Place_Encoding_Stimuli_Block_1_Run_1_df["encoding_stims"].tolist()
Pair_Encoding_Images_Block_1_Run_1 = Pair_Encoding_Stimuli_Block_1_Run_1_df["encoding_stims"].tolist()

# Create recognition list of images conditions
Face_Recog_Images_Block_1_Run_1 = Face_Recog_Stimuli_Block_1_Run_1_df["recog_stims"].tolist()
Place_Recog_Images_Block_1_Run_1 = Place_Recog_Stimuli_Block_1_Run_1_df["recog_stims"].tolist()
Pair_Recog_Images_Block_1_Run_1 = Pair_Recog_Stimuli_Block_1_Run_1_df["recog_stims"].tolist()

# Randomize each list
# BLOCK 1 RUN 1
random.shuffle(Face_Encoding_Images_Block_1_Run_1)
random.shuffle(Place_Encoding_Images_Block_1_Run_1)
random.shuffle(Pair_Encoding_Images_Block_1_Run_1)

random.shuffle(Face_Recog_Images_Block_1_Run_1)
random.shuffle(Place_Recog_Images_Block_1_Run_1)
random.shuffle(Pair_Recog_Images_Block_1_Run_1)

# Create a dictionary for encoding with keys for face, place, and pair encoding images
# and their respective randomized lists as values for Block 1 Run 1
Encoding_Dictionary_Block_1_Run_1 = {
    'Face_Encode_Key_Block_1_Run_1': Face_Encoding_Images_Block_1_Run_1,
    'Place_Encode_Key_Block_1_Run_1': Place_Encoding_Images_Block_1_Run_1,
    'Pair_Encode_Key_Block_1_Run_1': Pair_Encoding_Images_Block_1_Run_1
}

# Create a dictionary for recognition with keys for face, place, and pair recognition images
# and their respective randomized lists as values for Block 1 Run 1
Recognition_Dictionary_Block_1_Run_1 = {
    'Face_Recog_Key_Block_1_Run_1': Face_Recog_Images_Block_1_Run_1,
    'Place_Recog_Key_Block_1_Run_1': Place_Recog_Images_Block_1_Run_1,
    'Pair_Recog_Key_Block_1_Run_1': Pair_Recog_Images_Block_1_Run_1
}

# --- Initialize components for Routine "triggerSync" ---
triggerSyncText = visual.TextStim(win=win, name='triggerSyncText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
triggerSync_Key_Resp = keyboard.Keyboard()

# --- Initialize components for Routine "InstructionsText" ---
# Run 'Begin Experiment' code from InstructionCode
from psychopy.hardware import keyboard
from psychopy import core

# Function to set instruction message and time
def set_instruction_time_and_message(Block_1_Run_1_Started, Block_2_Run_2_Started, Block_3_Run_3_Started,
                                     Encoding_Started, Recognition_Started,
                                     Random_Encode_Key_Block_1_Run_1, Recog_Key_Block_1_Run_1
                                     ):

    # Initialize variables
    Instruction_Message = " "
    Instruction_Time = 10.0  # Instruction screen time

    # Block logic
    blocks_started = [Block_1_Run_1_Started, Block_2_Run_2_Started, Block_3_Run_3_Started]
    random_encode_keys = [Random_Encode_Key_Block_1_Run_1]
    recog_keys = [Recog_Key_Block_1_Run_1]

    for i in range(len(blocks_started)):
        if blocks_started[i] and not any(blocks_started[:i] + blocks_started[i+1:]):
            if Encoding_Started:
                if random_encode_keys[i] == f'Face_Encode_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Face_Encoding_Text
                elif random_encode_keys[i] == f'Place_Encode_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Place_Encoding_Text
                elif random_encode_keys[i] == f'Pair_Encode_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Pair_Encoding_Text

            elif Recognition_Started:
                if recog_keys[i] == f'Face_Recog_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Face_Recog_Text
                elif recog_keys[i] == f'Place_Recog_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Place_Recog_Text
                elif recog_keys[i] == f'Pair_Recog_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Pair_Recog_Text

    return Instruction_Time, Instruction_Message


                                
kb = keyboard.Keyboard()
timer_key = core.Clock()
start_time_key = 0
current_time_key = 0

# Text for encoding instruction screen 
# Face encoding condition text
Face_Encoding_Text = """
Male or female?

Index = male
Middle = female



"""
# Place encoding condition text
Place_Encoding_Text = """
Is there water in the scene?

Index = yes
Middle = no

"""

# Pair encoding condition text
Pair_Encoding_Text = """
Does the face "fit" with the scene?

Index = yes
Middle = no

"""

# Text for recognition instruction screen 
# Face recognition condition text
Face_Recog_Text = """
Was this face shown before?

Index = yes
Middle = no

"""
# Place recognition condition text
Place_Recog_Text = """
Was this scene shown before?

Index = yes
Middle = no

"""

# Pair recognition condition text
Pair_Recog_Text = """
Was this face shown together with this scene before?

Index = yes
Middle = no

"""
InstructionText = visual.TextStim(win=win, name='InstructionText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "encodeTrial_Run1" ---
# Run 'Begin Experiment' code from encodeTrialRun1Code
from psychopy.hardware import keyboard
from psychopy import core

# Function to store encode condition status and subject response
def update_encode_pre_recog_response_data(block_num, run_num, current_displayed_image, random_encode_key, response_key, liquid_conditions):
    gender_is_correct = None
    liquid_is_correct = None
    response_pair_fit = None

    image_gender = None
    response_gender = None
    image_water = None
    response_water = None
    response_pair_fit = None

    # Face encode condition
    if random_encode_key == f'Face_Encode_Key_Block_{block_num}_Run_{run_num}':
         image_gender = 'male' if 'om' in current_displayed_image or 'ym' in current_displayed_image else 'female'
         
         if response_key == '1':
            response_gender = 'male'
         elif response_key == '2':
            response_gender = 'female'
         else:
            response_gender = 'none'
         
         gender_is_correct = 'NO RESPONSE' if response_gender == 'none' else response_gender == image_gender
    
    # Place encode condition
    elif random_encode_key == f'Place_Encode_Key_Block_{block_num}_Run_{run_num}':
        image_water = 'no_liquid'
        for substr in liquid_conditions:
            if substr in current_displayed_image:
                image_water = 'liquid'
                break
    
        if response_key == '1':
            response_water = 'liquid'
        elif response_key == '2':
            response_water = 'no_liquid'
        else:
            response_water = 'none'
   
        liquid_is_correct = 'NO RESPONSE' if response_water == 'none' else response_water == image_water
    
    # Pair encode condition
    elif random_encode_key == f'Pair_Encode_Key_Block_{block_num}_Run_{run_num}':
        
        if response_key == '1':
            response_pair_fit = 'fits'
        elif response_key == '2':
            response_pair_fit = 'does_not_fit'
        else:
            response_pair_fit = 'none'

    return gender_is_correct, liquid_is_correct, response_pair_fit, image_gender, response_gender, image_water, response_water, response_pair_fit

kb = keyboard.Keyboard()
timer_key = core.Clock()
start_time_key = 0
current_time_key = 0

# Initialize the encoding lists to store encoding txt data
Encoding_Data_Face_Block_1_Run_1 = []
Encoding_Data_Place_Block_1_Run_1 = []
Encoding_Data_Pair_Block_1_Run_1 = []

# Initialize the encoding response data as dictionaries
Encoding_Response_Data_Face_Block_1_Run_1 = {}
Encoding_Response_Data_Place_Block_1_Run_1 = {}
Encoding_Response_Data_Pair_Block_1_Run_1 = {}

# Initialize the image_start_time variable
image_start_time = 0



encodeTrialRun1_Image = visual.ImageStim(
    win=win,
    name='encodeTrialRun1_Image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.33, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
encodeFixationText_Run1 = visual.TextStim(win=win, name='encodeFixationText_Run1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
encodeTrialTestKeyRespRun1 = keyboard.Keyboard()

# --- Initialize components for Routine "InstructionsText" ---
# Run 'Begin Experiment' code from InstructionCode
from psychopy.hardware import keyboard
from psychopy import core

# Function to set instruction message and time
def set_instruction_time_and_message(Block_1_Run_1_Started, Block_2_Run_2_Started, Block_3_Run_3_Started,
                                     Encoding_Started, Recognition_Started,
                                     Random_Encode_Key_Block_1_Run_1, Recog_Key_Block_1_Run_1
                                     ):

    # Initialize variables
    Instruction_Message = " "
    Instruction_Time = 10.0  # Instruction screen time

    # Block logic
    blocks_started = [Block_1_Run_1_Started, Block_2_Run_2_Started, Block_3_Run_3_Started]
    random_encode_keys = [Random_Encode_Key_Block_1_Run_1]
    recog_keys = [Recog_Key_Block_1_Run_1]

    for i in range(len(blocks_started)):
        if blocks_started[i] and not any(blocks_started[:i] + blocks_started[i+1:]):
            if Encoding_Started:
                if random_encode_keys[i] == f'Face_Encode_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Face_Encoding_Text
                elif random_encode_keys[i] == f'Place_Encode_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Place_Encoding_Text
                elif random_encode_keys[i] == f'Pair_Encode_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Pair_Encoding_Text

            elif Recognition_Started:
                if recog_keys[i] == f'Face_Recog_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Face_Recog_Text
                elif recog_keys[i] == f'Place_Recog_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Place_Recog_Text
                elif recog_keys[i] == f'Pair_Recog_Key_Block_{i+1}_Run_{i+1}':
                    Instruction_Message = Pair_Recog_Text

    return Instruction_Time, Instruction_Message


                                
kb = keyboard.Keyboard()
timer_key = core.Clock()
start_time_key = 0
current_time_key = 0

# Text for encoding instruction screen 
# Face encoding condition text
Face_Encoding_Text = """
Male or female?

Index = male
Middle = female



"""
# Place encoding condition text
Place_Encoding_Text = """
Is there water in the scene?

Index = yes
Middle = no

"""

# Pair encoding condition text
Pair_Encoding_Text = """
Does the face "fit" with the scene?

Index = yes
Middle = no

"""

# Text for recognition instruction screen 
# Face recognition condition text
Face_Recog_Text = """
Was this face shown before?

Index = yes
Middle = no

"""
# Place recognition condition text
Place_Recog_Text = """
Was this scene shown before?

Index = yes
Middle = no

"""

# Pair recognition condition text
Pair_Recog_Text = """
Was this face shown together with this scene before?

Index = yes
Middle = no

"""
InstructionText = visual.TextStim(win=win, name='InstructionText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "recognitionTrial_Run1" ---
# Run 'Begin Experiment' code from recognitonTrialRun1Code
from psychopy.hardware import keyboard
from psychopy import core

# Function to store recognition response for d-prime
def d_prime(image_old_new, response_key):
    is_correct = None

    # "OLD" images condition
    if image_old_new == "OLD":
        if response_key == '1':
            is_correct = 'HIT'
        elif response_key == '2':
            is_correct = 'MISS'
        else:
            is_correct = 'NO RESPONSE'

    # "NEW" images condition
    elif image_old_new == "NEW":
        if response_key == '1':
            is_correct = 'FALSE ALARM'
        elif response_key == '2':
            is_correct = 'CORRECT REJECTION'
        else:
            is_correct = "NO RESPONSE"

    return is_correct

# Function to update encoding and recognition txt lists based on d - prime
def update_encoding_recognition_response_data( 
    block_num,  
    run_num, 
    is_correct, 
    current_displayed_image, 
    recog_key, 
    image_start_time, 
    image_time, 
    recog_response_data_face, 
    recog_response_data_place, 
    recog_response_data_pair, 
    encoding_response_data_face, 
    encoding_response_data_place, 
    encoding_response_data_pair
):

    # If the response is correct
    if is_correct == 'HIT' or is_correct == 'CORRECT REJECTION':
        # Add to txt only if responses are correct 
        if recog_key == f'Face_Recog_Key_Block_{block_num}_Run_{run_num}':
            recog_response_data_face.append([image_start_time, image_time, 1.000])
        elif recog_key == f'Place_Recog_Key_Block_{block_num}_Run_{run_num}':
            recog_response_data_place.append([image_start_time, image_time, 1.000])
        elif recog_key == f'Pair_Recog_Key_Block_{block_num}_Run_{run_num}':
            recog_response_data_pair.append([image_start_time, image_time, 1.000])

    else: 
        # If the response is incorrect or no response, remove the data for the image from encoding txt response
        
        # Modify the recognition image path to match the encoding phase image path
        encoding_image_path = current_displayed_image.replace('_Recog', '_Encoding')

        if recog_key == f'Face_Recog_Key_Block_{block_num}_Run_{run_num}':
            if encoding_image_path in encoding_response_data_face:
                encoding_response_data_face.pop(encoding_image_path, None)
        elif recog_key == f'Place_Recog_Key_Block_{block_num}_Run_{run_num}':
            if encoding_image_path in encoding_response_data_place:
                encoding_response_data_place.pop(encoding_image_path, None)
        elif recog_key == f'Pair_Recog_Key_Block_{block_num}_Run_{run_num}':
            if encoding_image_path in encoding_response_data_pair:
                encoding_response_data_pair.pop(encoding_image_path, None)


# Create a keyboard object and a timer for the keyboard
kb = keyboard.Keyboard()
timer_key = core.Clock()

start_time_key = 0
current_time_key = 0

# Initialize the recognition lists to store recognition data
Recog_Data_Face_Block_1_Run_1 = []
Recog_Data_Place_Block_1_Run_1 = []
Recog_Data_Pair_Block_1_Run_1 = []

# Initialize the encoding lists to store encoding txt data based on recognition responses
Recog_Response_Data_Face_Block_1_Run_1 = []
Recog_Response_Data_Place_Block_1_Run_1 = []
Recog_Response_Data_Pair_Block_1_Run_1 = []
recogTrialRun1_Image = visual.ImageStim(
    win=win,
    name='recogTrialRun1_Image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1.33, 1.0),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
recogFixationText_Run1 = visual.TextStim(win=win, name='recogFixationText_Run1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
recogTrialTestKeyRespRun1 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "setUp" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
setUpComponents = []
for thisComponent in setUpComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "setUp" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setUpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "setUp" ---
for thisComponent in setUpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setUp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
condLoaderLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='condLoaderLoop')
thisExp.addLoop(condLoaderLoop)  # add the loop to the experiment
thisCondLoaderLoop = condLoaderLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondLoaderLoop.rgb)
if thisCondLoaderLoop != None:
    for paramName in thisCondLoaderLoop:
        exec('{} = thisCondLoaderLoop[paramName]'.format(paramName))

for thisCondLoaderLoop in condLoaderLoop:
    currentLoop = condLoaderLoop
    # abbreviate parameter names if possible (e.g. rgb = thisCondLoaderLoop.rgb)
    if thisCondLoaderLoop != None:
        for paramName in thisCondLoaderLoop:
            exec('{} = thisCondLoaderLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "condLoader" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from condLoaderCode
    import random
    
    # BLOCK 1 RUN 1
    # Create a list of encoding dictionary keys and shuffle them
    Encode_Key_List_Block_1_Run_1 = list(Encoding_Dictionary_Block_1_Run_1.keys())
    random.shuffle(Encode_Key_List_Block_1_Run_1 )
    
    # Get a random encoding key and its corresponding encoding list from the shuffled keys
    Random_Encode_Key_Block_1_Run_1 = Encode_Key_List_Block_1_Run_1[current_encode_key_index]
    Random_Encode_List_Block_1_Run_1 = Encoding_Dictionary_Block_1_Run_1[Random_Encode_Key_Block_1_Run_1]
    
    # Determine the corresponding recognition key based on the chosen encoding key
    if Random_Encode_Key_Block_1_Run_1  == 'Face_Encode_Key_Block_1_Run_1':
        Recog_Key_Block_1_Run_1 = 'Face_Recog_Key_Block_1_Run_1'
    elif Random_Encode_Key_Block_1_Run_1 == 'Place_Encode_Key_Block_1_Run_1':
        Recog_Key_Block_1_Run_1 = 'Place_Recog_Key_Block_1_Run_1'
    elif Random_Encode_Key_Block_1_Run_1 == 'Pair_Encode_Key_Block_1_Run_1':
        Recog_Key_Block_1_Run_1 = 'Pair_Recog_Key_Block_1_Run_1'
    
    # Get the corresponding recognition list based on the determined recognition key
    Recog_List_Block_1_Run_1 = Recognition_Dictionary_Block_1_Run_1[Recog_Key_Block_1_Run_1]
    # keep track of which components have finished
    condLoaderComponents = []
    for thisComponent in condLoaderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "condLoader" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in condLoaderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "condLoader" ---
    for thisComponent in condLoaderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "condLoader" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'condLoaderLoop'


# --- Prepare to start Routine "triggerSync" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from triggerSyncCode
trigger_sync_message = "+"
if volume_counter == 1:
    trigger_sync_message = "Waiting for scanner..."




triggerSyncText.setText(trigger_sync_message)
triggerSync_Key_Resp.keys = []
triggerSync_Key_Resp.rt = []
_triggerSync_Key_Resp_allKeys = []
# keep track of which components have finished
triggerSyncComponents = [triggerSyncText, triggerSync_Key_Resp]
for thisComponent in triggerSyncComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "triggerSync" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *triggerSyncText* updates
    if triggerSyncText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        triggerSyncText.frameNStart = frameN  # exact frame index
        triggerSyncText.tStart = t  # local t and not account for scr refresh
        triggerSyncText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(triggerSyncText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'triggerSyncText.started')
        triggerSyncText.setAutoDraw(True)
    
    # *triggerSync_Key_Resp* updates
    waitOnFlip = False
    if triggerSync_Key_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        triggerSync_Key_Resp.frameNStart = frameN  # exact frame index
        triggerSync_Key_Resp.tStart = t  # local t and not account for scr refresh
        triggerSync_Key_Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(triggerSync_Key_Resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'triggerSync_Key_Resp.started')
        triggerSync_Key_Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(triggerSync_Key_Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(triggerSync_Key_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if triggerSync_Key_Resp.status == STARTED and not waitOnFlip:
        theseKeys = triggerSync_Key_Resp.getKeys(keyList=['5','t','s'], waitRelease=False)
        _triggerSync_Key_Resp_allKeys.extend(theseKeys)
        if len(_triggerSync_Key_Resp_allKeys):
            triggerSync_Key_Resp.keys = _triggerSync_Key_Resp_allKeys[-1].name  # just the last key pressed
            triggerSync_Key_Resp.rt = _triggerSync_Key_Resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerSyncComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "triggerSync" ---
for thisComponent in triggerSyncComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if triggerSync_Key_Resp.keys in ['', [], None]:  # No response was made
    triggerSync_Key_Resp.keys = None
thisExp.addData('triggerSync_Key_Resp.keys',triggerSync_Key_Resp.keys)
if triggerSync_Key_Resp.keys != None:  # we had a response
    thisExp.addData('triggerSync_Key_Resp.rt', triggerSync_Key_Resp.rt)
thisExp.nextEntry()
# the Routine "triggerSync" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Block1Loop = data.TrialHandler(nReps=3.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Block1Loop')
thisExp.addLoop(Block1Loop)  # add the loop to the experiment
thisBlock1Loop = Block1Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1Loop.rgb)
if thisBlock1Loop != None:
    for paramName in thisBlock1Loop:
        exec('{} = thisBlock1Loop[paramName]'.format(paramName))

for thisBlock1Loop in Block1Loop:
    currentLoop = Block1Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1Loop.rgb)
    if thisBlock1Loop != None:
        for paramName in thisBlock1Loop:
            exec('{} = thisBlock1Loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "InstructionsText" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from InstructionCode
    if(volume_counter == 1):
        start_time = timer.getTime();
        
    # Set Instruction Message and time to 10.0 if not fixation cross
    Instruction_Time, Instruction_Message = set_instruction_time_and_message(
        Block_1_Run_1_Started, Block_2_Run_2_Started, Block_3_Run_3_Started,
        Encoding_Started, Recognition_Started,
        Random_Encode_Key_Block_1_Run_1, Recog_Key_Block_1_Run_1
        
    )
    
    current_time = timer.getTime() - start_time
    thisExp.addData('start_time',current_time)
    
    thisExp.addData('start_volume',volume_counter)
    kb.clock.reset()  # when you want to start the timer from
    volume_counter_message = str(volume_counter)+" out of "+str(volume_total)
    # keep track of which components have finished
    InstructionsTextComponents = [InstructionText]
    for thisComponent in InstructionsTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstructionsText" ---
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from InstructionCode
        # during your trial
        keys = kb.getKeys(['5','t','s'], waitRelease=True)
        for key in keys:
            if volume_counter <= 1:
                start_time_key = timer_key.getTime()
                current_time_key = timer_key.getTime() - start_time_key
            else:
                current_time_key = timer_key.getTime() - start_time_key
                start_time_key = timer_key.getTime()
            
            thisExp.addData('trigger_time', current_time_key)
            
            thisExp.addData('end_volume',volume_counter)
            volume_counter_message = str(volume_counter)+" out of "+str(volume_total)
            volume_counter += 1
            print(volume_counter_message)
        
        
        # *InstructionText* updates
        if InstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionText.frameNStart = frameN  # exact frame index
            InstructionText.tStart = t  # local t and not account for scr refresh
            InstructionText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionText.started')
            InstructionText.setAutoDraw(True)
        if InstructionText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > InstructionText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                InstructionText.tStop = t  # not accounting for scr refresh
                InstructionText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'InstructionText.stopped')
                InstructionText.setAutoDraw(False)
        if InstructionText.status == STARTED:  # only update if drawing
            InstructionText.setText(Instruction_Message, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionsText" ---
    for thisComponent in InstructionsTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    
    # set up handler to look after randomisation of conditions etc
    encodeLoop_Block1Run1 = data.TrialHandler(nReps=12.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='encodeLoop_Block1Run1')
    thisExp.addLoop(encodeLoop_Block1Run1)  # add the loop to the experiment
    thisEncodeLoop_Block1Run1 = encodeLoop_Block1Run1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncodeLoop_Block1Run1.rgb)
    if thisEncodeLoop_Block1Run1 != None:
        for paramName in thisEncodeLoop_Block1Run1:
            exec('{} = thisEncodeLoop_Block1Run1[paramName]'.format(paramName))
    
    for thisEncodeLoop_Block1Run1 in encodeLoop_Block1Run1:
        currentLoop = encodeLoop_Block1Run1
        # abbreviate parameter names if possible (e.g. rgb = thisEncodeLoop_Block1Run1.rgb)
        if thisEncodeLoop_Block1Run1 != None:
            for paramName in thisEncodeLoop_Block1Run1:
                exec('{} = thisEncodeLoop_Block1Run1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "encodeTrial_Run1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from encodeTrialRun1Code
        # Add the start time and volume counter to the data
        thisExp.addData('start_volume',volume_counter)
        
        kb.clock.reset()  # when you want to start the timer from
        volume_counter_message = str(volume_counter)+" out of "+str(volume_total)
        
        current_time_key = 0
        
        # Update the current_displayed_image variable
        current_displayed_image = Random_Encode_List_Block_1_Run_1[current_encode_index]
        
        # Add the image_file data
        thisExp.addData('image_file', current_displayed_image)
        
        # Add the run to the data
        thisExp.addData('run', Block_1_Run)
        
        
        encodeTrialTestKeyRespRun1.keys = []
        encodeTrialTestKeyRespRun1.rt = []
        _encodeTrialTestKeyRespRun1_allKeys = []
        # keep track of which components have finished
        encodeTrial_Run1Components = [encodeTrialRun1_Image, encodeFixationText_Run1, encodeTrialTestKeyRespRun1]
        for thisComponent in encodeTrial_Run1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "encodeTrial_Run1" ---
        while continueRoutine and routineTimer.getTime() < 9.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from encodeTrialRun1Code
            # during your trial
            keys = kb.getKeys(['5','t','s'], waitRelease=True)
            for key in keys:
                if volume_counter <= 1:
                    start_time_key = timer_key.getTime()
                    current_time_key = timer_key.getTime() - start_time_key
                else:
                    current_time_key = timer_key.getTime() - start_time_key
                    start_time_key = timer_key.getTime()
                
                thisExp.addData('trigger_time', current_time_key)
                
                thisExp.addData('end_volume',volume_counter)
                volume_counter_message = str(volume_counter)+" out of "+str(volume_total)
                volume_counter += 1
                print(volume_counter_message)
            
            
            
            
            
            
            
            # *encodeTrialRun1_Image* updates
            if encodeTrialRun1_Image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                encodeTrialRun1_Image.frameNStart = frameN  # exact frame index
                encodeTrialRun1_Image.tStart = t  # local t and not account for scr refresh
                encodeTrialRun1_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encodeTrialRun1_Image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'encodeTrialRun1_Image.started')
                encodeTrialRun1_Image.setAutoDraw(True)
            if encodeTrialRun1_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encodeTrialRun1_Image.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    encodeTrialRun1_Image.tStop = t  # not accounting for scr refresh
                    encodeTrialRun1_Image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'encodeTrialRun1_Image.stopped')
                    encodeTrialRun1_Image.setAutoDraw(False)
            if encodeTrialRun1_Image.status == STARTED:  # only update if drawing
                encodeTrialRun1_Image.setImage(Random_Encode_List_Block_1_Run_1[current_encode_index], log=False)
            
            # *encodeFixationText_Run1* updates
            if encodeFixationText_Run1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                encodeFixationText_Run1.frameNStart = frameN  # exact frame index
                encodeFixationText_Run1.tStart = t  # local t and not account for scr refresh
                encodeFixationText_Run1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encodeFixationText_Run1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'encodeFixationText_Run1.started')
                encodeFixationText_Run1.setAutoDraw(True)
            if encodeFixationText_Run1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encodeFixationText_Run1.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    encodeFixationText_Run1.tStop = t  # not accounting for scr refresh
                    encodeFixationText_Run1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'encodeFixationText_Run1.stopped')
                    encodeFixationText_Run1.setAutoDraw(False)
            if encodeFixationText_Run1.status == STARTED:  # only update if drawing
                encodeFixationText_Run1.setText('+', log=False)
            
            # *encodeTrialTestKeyRespRun1* updates
            waitOnFlip = False
            if encodeTrialTestKeyRespRun1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                encodeTrialTestKeyRespRun1.frameNStart = frameN  # exact frame index
                encodeTrialTestKeyRespRun1.tStart = t  # local t and not account for scr refresh
                encodeTrialTestKeyRespRun1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(encodeTrialTestKeyRespRun1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'encodeTrialTestKeyRespRun1.started')
                encodeTrialTestKeyRespRun1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(encodeTrialTestKeyRespRun1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(encodeTrialTestKeyRespRun1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if encodeTrialTestKeyRespRun1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > encodeTrialTestKeyRespRun1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    encodeTrialTestKeyRespRun1.tStop = t  # not accounting for scr refresh
                    encodeTrialTestKeyRespRun1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'encodeTrialTestKeyRespRun1.stopped')
                    encodeTrialTestKeyRespRun1.status = FINISHED
            if encodeTrialTestKeyRespRun1.status == STARTED and not waitOnFlip:
                theseKeys = encodeTrialTestKeyRespRun1.getKeys(keyList=['1','2'], waitRelease=False)
                _encodeTrialTestKeyRespRun1_allKeys.extend(theseKeys)
                if len(_encodeTrialTestKeyRespRun1_allKeys):
                    encodeTrialTestKeyRespRun1.keys = _encodeTrialTestKeyRespRun1_allKeys[-1].name  # just the last key pressed
                    encodeTrialTestKeyRespRun1.rt = _encodeTrialTestKeyRespRun1_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in encodeTrial_Run1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "encodeTrial_Run1" ---
        for thisComponent in encodeTrial_Run1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from encodeTrialRun1Code
        # Calculate and add the end time to the data
        current_time = timer.getTime() - start_time
        thisExp.addData('end_time', current_time)
        
        # Record encoding response
        gender_is_correct, liquid_is_correct, pair_fit_is_correct, image_gender, response_gender, image_water, response_water, response_pair_fit = update_encode_pre_recog_response_data(
            block_num=1,
            run_num=Block_1_Run,
            current_displayed_image=current_displayed_image,
            random_encode_key=Random_Encode_Key_Block_1_Run_1,
            response_key=encodeTrialTestKeyRespRun1.keys,
            liquid_conditions=["beach2", "beach3", "city1", "citybeach10", "hills13","hills15"]
        )
        
        # Save encoding responses to output
        if gender_is_correct is not None:
            thisExp.addData('image_gender', image_gender)
            thisExp.addData('response_gender', response_gender)
            thisExp.addData('gender_is_correct', gender_is_correct)
        
        if liquid_is_correct is not None:
            thisExp.addData('image_water', image_water)
            thisExp.addData('response_water', response_water)
            thisExp.addData('liquid_is_correct', liquid_is_correct)
        
        if response_pair_fit is not None:
            thisExp.addData('response_pair_fit', response_pair_fit)
        
        # For resetting volume_counter based on Block loop iteration 
        Block_Loop_Voulme_Counter.append(Block1Loop.thisRepN)
        
        # Increment the current encode index to iterate over images
        current_encode_index += 1
        
        if current_encode_index == 1: # First stimulus is shown
            Fix_Cross_Started = True # Next ISI is '+'
            encode_trials_counter += 1
        
        if current_encode_index == 12: # Last stimulus is shown
            
            current_encode_index = 0 # Reset stimulus counter
            current_encode_key_index += 1 # Next encode condition
            current_jitter_index = 0 # Reset current jitter index
            
            Encoding_Started = False # End of encoding 
            Fix_Cross_Started = False # Next ISI is instructions
            Recognition_Started = True # Start of recognition
            
                
            if current_encode_key_index == 3: # At last encoding condition
                current_encode_key_index = 0 # Reset encode condition order
            else:
                Random_Encode_Key_Block_1_Run_1 = Encode_Key_List_Block_1_Run_1[current_encode_key_index]
                Random_Encode_List_Block_1_Run_1 = Encoding_Dictionary_Block_1_Run_1[Random_Encode_Key_Block_1_Run_1]
             
        if Fix_Cross_Started == True:
            current_jitter_index += 1
         
        
        # check responses
        if encodeTrialTestKeyRespRun1.keys in ['', [], None]:  # No response was made
            encodeTrialTestKeyRespRun1.keys = None
        encodeLoop_Block1Run1.addData('encodeTrialTestKeyRespRun1.keys',encodeTrialTestKeyRespRun1.keys)
        if encodeTrialTestKeyRespRun1.keys != None:  # we had a response
            encodeLoop_Block1Run1.addData('encodeTrialTestKeyRespRun1.rt', encodeTrialTestKeyRespRun1.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-9.000000)
        thisExp.nextEntry()
        
    # completed 12.0 repeats of 'encodeLoop_Block1Run1'
    
    
    # --- Prepare to start Routine "InstructionsText" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from InstructionCode
    if(volume_counter == 1):
        start_time = timer.getTime();
        
    # Set Instruction Message and time to 10.0 if not fixation cross
    Instruction_Time, Instruction_Message = set_instruction_time_and_message(
        Block_1_Run_1_Started, Block_2_Run_2_Started, Block_3_Run_3_Started,
        Encoding_Started, Recognition_Started,
        Random_Encode_Key_Block_1_Run_1, Recog_Key_Block_1_Run_1
        
    )
    
    current_time = timer.getTime() - start_time
    thisExp.addData('start_time',current_time)
    
    thisExp.addData('start_volume',volume_counter)
    kb.clock.reset()  # when you want to start the timer from
    volume_counter_message = str(volume_counter)+" out of "+str(volume_total)
    # keep track of which components have finished
    InstructionsTextComponents = [InstructionText]
    for thisComponent in InstructionsTextComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "InstructionsText" ---
    while continueRoutine and routineTimer.getTime() < 10.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from InstructionCode
        # during your trial
        keys = kb.getKeys(['5','t','s'], waitRelease=True)
        for key in keys:
            if volume_counter <= 1:
                start_time_key = timer_key.getTime()
                current_time_key = timer_key.getTime() - start_time_key
            else:
                current_time_key = timer_key.getTime() - start_time_key
                start_time_key = timer_key.getTime()
            
            thisExp.addData('trigger_time', current_time_key)
            
            thisExp.addData('end_volume',volume_counter)
            volume_counter_message = str(volume_counter)+" out of "+str(volume_total)
            volume_counter += 1
            print(volume_counter_message)
        
        
        # *InstructionText* updates
        if InstructionText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionText.frameNStart = frameN  # exact frame index
            InstructionText.tStart = t  # local t and not account for scr refresh
            InstructionText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionText.started')
            InstructionText.setAutoDraw(True)
        if InstructionText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > InstructionText.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                InstructionText.tStop = t  # not accounting for scr refresh
                InstructionText.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'InstructionText.stopped')
                InstructionText.setAutoDraw(False)
        if InstructionText.status == STARTED:  # only update if drawing
            InstructionText.setText(Instruction_Message, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in InstructionsTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "InstructionsText" ---
    for thisComponent in InstructionsTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-10.000000)
    
    # set up handler to look after randomisation of conditions etc
    recognitionLoop_Block1Run1 = data.TrialHandler(nReps=12.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='recognitionLoop_Block1Run1')
    thisExp.addLoop(recognitionLoop_Block1Run1)  # add the loop to the experiment
    thisRecognitionLoop_Block1Run1 = recognitionLoop_Block1Run1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecognitionLoop_Block1Run1.rgb)
    if thisRecognitionLoop_Block1Run1 != None:
        for paramName in thisRecognitionLoop_Block1Run1:
            exec('{} = thisRecognitionLoop_Block1Run1[paramName]'.format(paramName))
    
    for thisRecognitionLoop_Block1Run1 in recognitionLoop_Block1Run1:
        currentLoop = recognitionLoop_Block1Run1
        # abbreviate parameter names if possible (e.g. rgb = thisRecognitionLoop_Block1Run1.rgb)
        if thisRecognitionLoop_Block1Run1 != None:
            for paramName in thisRecognitionLoop_Block1Run1:
                exec('{} = thisRecognitionLoop_Block1Run1[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "recognitionTrial_Run1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from recognitonTrialRun1Code
        # Add the start time and volume counter to the data
        thisExp.addData('start_volume', volume_counter)
        
        # Reset the keyboard clock
        kb.clock.reset()  # when you want to start the timer from
        
        # Set the volume counter message
        volume_counter_message = str(volume_counter) + " out of " + str(volume_total)
        
        current_time_key = 0
        
        # Update the current_displayed_image variable
        current_displayed_image = Recog_List_Block_1_Run_1[current_recog_index]
        
        # Add the current_displayed_image to the data
        thisExp.addData('image_file', current_displayed_image)
        
        # Add the run to the data
        thisExp.addData('run', Block_1_Run)
        
        
        recogTrialTestKeyRespRun1.keys = []
        recogTrialTestKeyRespRun1.rt = []
        _recogTrialTestKeyRespRun1_allKeys = []
        # keep track of which components have finished
        recognitionTrial_Run1Components = [recogTrialRun1_Image, recogFixationText_Run1, recogTrialTestKeyRespRun1]
        for thisComponent in recognitionTrial_Run1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "recognitionTrial_Run1" ---
        while continueRoutine and routineTimer.getTime() < 9.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from recognitonTrialRun1Code
            # during your trial
            keys = kb.getKeys(['5','t','s'], waitRelease=True)
            for key in keys:
                if volume_counter <= 1:
                    start_time_key = timer_key.getTime()
                    current_time_key = timer_key.getTime() - start_time_key
                else:
                    current_time_key = timer_key.getTime() - start_time_key
                    start_time_key = timer_key.getTime()
                
                thisExp.addData('trigger_time', current_time_key)
                
                thisExp.addData('end_volume',volume_counter)
                volume_counter_message = str(volume_counter)+" out of "+str(volume_total)
                volume_counter += 1
                print(volume_counter_message)
            
            
            # *recogTrialRun1_Image* updates
            if recogTrialRun1_Image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recogTrialRun1_Image.frameNStart = frameN  # exact frame index
                recogTrialRun1_Image.tStart = t  # local t and not account for scr refresh
                recogTrialRun1_Image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recogTrialRun1_Image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recogTrialRun1_Image.started')
                recogTrialRun1_Image.setAutoDraw(True)
            if recogTrialRun1_Image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recogTrialRun1_Image.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    recogTrialRun1_Image.tStop = t  # not accounting for scr refresh
                    recogTrialRun1_Image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recogTrialRun1_Image.stopped')
                    recogTrialRun1_Image.setAutoDraw(False)
            if recogTrialRun1_Image.status == STARTED:  # only update if drawing
                recogTrialRun1_Image.setImage(Recog_List_Block_1_Run_1[current_recog_index], log=False)
            
            # *recogFixationText_Run1* updates
            if recogFixationText_Run1.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
                # keep track of start time/frame for later
                recogFixationText_Run1.frameNStart = frameN  # exact frame index
                recogFixationText_Run1.tStart = t  # local t and not account for scr refresh
                recogFixationText_Run1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recogFixationText_Run1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recogFixationText_Run1.started')
                recogFixationText_Run1.setAutoDraw(True)
            if recogFixationText_Run1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recogFixationText_Run1.tStartRefresh + 6.0-frameTolerance:
                    # keep track of stop time/frame for later
                    recogFixationText_Run1.tStop = t  # not accounting for scr refresh
                    recogFixationText_Run1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recogFixationText_Run1.stopped')
                    recogFixationText_Run1.setAutoDraw(False)
            if recogFixationText_Run1.status == STARTED:  # only update if drawing
                recogFixationText_Run1.setText('+', log=False)
            
            # *recogTrialTestKeyRespRun1* updates
            waitOnFlip = False
            if recogTrialTestKeyRespRun1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                recogTrialTestKeyRespRun1.frameNStart = frameN  # exact frame index
                recogTrialTestKeyRespRun1.tStart = t  # local t and not account for scr refresh
                recogTrialTestKeyRespRun1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(recogTrialTestKeyRespRun1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'recogTrialTestKeyRespRun1.started')
                recogTrialTestKeyRespRun1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(recogTrialTestKeyRespRun1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(recogTrialTestKeyRespRun1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if recogTrialTestKeyRespRun1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > recogTrialTestKeyRespRun1.tStartRefresh + 6-frameTolerance:
                    # keep track of stop time/frame for later
                    recogTrialTestKeyRespRun1.tStop = t  # not accounting for scr refresh
                    recogTrialTestKeyRespRun1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'recogTrialTestKeyRespRun1.stopped')
                    recogTrialTestKeyRespRun1.status = FINISHED
            if recogTrialTestKeyRespRun1.status == STARTED and not waitOnFlip:
                theseKeys = recogTrialTestKeyRespRun1.getKeys(keyList=['1','2'], waitRelease=False)
                _recogTrialTestKeyRespRun1_allKeys.extend(theseKeys)
                if len(_recogTrialTestKeyRespRun1_allKeys):
                    recogTrialTestKeyRespRun1.keys = _recogTrialTestKeyRespRun1_allKeys[-1].name  # just the last key pressed
                    recogTrialTestKeyRespRun1.rt = _recogTrialTestKeyRespRun1_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in recognitionTrial_Run1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "recognitionTrial_Run1" ---
        for thisComponent in recognitionTrial_Run1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from recognitonTrialRun1Code
        # Calculate and add the end time to the data
        current_time = timer.getTime() - start_time
        thisExp.addData('end_time', current_time)
        
        # Get the image OLD/NEW status and determine if the response is correct
        image_name = Recog_List_Block_1_Run_1[current_recog_index]
        if 'OLD' in image_name:
            image_old_new = "OLD"
        else:
            image_old_new = "NEW"
        # Add the image_old_new data to the experiment handler before response_old_new
        thisExp.addData('image_old_new', image_old_new)
        
        # Get the participant's response for the recognition trial
        if recogTrialTestKeyRespRun1.keys == '1':
            response_old_new = "OLD"
        elif recogTrialTestKeyRespRun1.keys == '2':
            response_old_new = "NEW"
        else:
            response_old_new = "NONE"
        # Add the response_old_new data to the experiment handler
        thisExp.addData('response_old_new', response_old_new)
        
        # Determine d prime and add results to the experiment handler
        is_correct = d_prime(image_old_new=image_old_new, response_key=recogTrialTestKeyRespRun1.keys)
        thisExp.addData('is_correct', is_correct)
        
        # Update encoding and recognition txt response list
        update_encoding_recognition_response_data(
            block_num=1, # Change based on block number
            run_num=Block_1_Run,  # Change based on run number
            is_correct=is_correct, 
            current_displayed_image=current_displayed_image, 
            recog_key=Recog_Key_Block_1_Run_1, # Change based on Block and condition
            image_start_time=image_start_time, 
            image_time=image_time, 
            recog_response_data_face=Recog_Response_Data_Face_Block_1_Run_1,  # Change based on Block and condition
            recog_response_data_place=Recog_Response_Data_Place_Block_1_Run_1,  # Change based on Block and condition
            recog_response_data_pair=Recog_Response_Data_Pair_Block_1_Run_1,  # Change based on Block and condition
            encoding_response_data_face=Encoding_Response_Data_Face_Block_1_Run_1,  # Change based on Block and condition
            encoding_response_data_place=Encoding_Response_Data_Place_Block_1_Run_1,  # Change based on Block and condition
            encoding_response_data_pair=Encoding_Response_Data_Pair_Block_1_Run_1  # Change based on Block and condition
        )
        
        # Increment the current recognition index to iterate over images
        current_recog_index += 1
        
        if current_recog_index == 1: # First stimulus is shown
            Fix_Cross_Started = True # Next ISI is '+'
            recognition_trials_counter += 1
            
        if current_recog_index == 12: # Last stimulus is shown
            # Increment the number of trialis in block loop
            block_loop_trials_counter += 1
            
            Recognition_Started = False # End of recognition
            Fix_Cross_Started = False # Next ISI is instructions
            Encoding_Started = True # Start of encoding 
                
            # Reset the current recognition index 
            current_recog_index = 0
            
            # Reset current jitter index
            current_jitter_index = 0
            
            # Determine the corresponding recognition key based on the chosen encoding key
            if Random_Encode_Key_Block_1_Run_1  == 'Face_Encode_Key_Block_1_Run_1':
                Recog_Key_Block_1_Run_1 = 'Face_Recog_Key_Block_1_Run_1'
            elif Random_Encode_Key_Block_1_Run_1 == 'Place_Encode_Key_Block_1_Run_1':
                Recog_Key_Block_1_Run_1 = 'Place_Recog_Key_Block_1_Run_1'
            elif Random_Encode_Key_Block_1_Run_1 == 'Pair_Encode_Key_Block_1_Run_1':
                Recog_Key_Block_1_Run_1 = 'Pair_Recog_Key_Block_1_Run_1'
        
            # Get the corresponding recognition list based on the determined recognition key
            Recog_List_Block_1_Run_1 = Recognition_Dictionary_Block_1_Run_1[Recog_Key_Block_1_Run_1]
        
        
        # Iterate through jitter times if showing fixation cross and after first image
        if Fix_Cross_Started == True:
            current_jitter_index += 1
         
        # Reset the trial counters
        if block_loop_trials_counter == 3:
            block_loop_trials_counter = 0
            recognition_trials_counter = 0
            encode_trials_counter = 0
        
        # For resetting volume_counter based on Block loop iteration 
        Block_Loop_Voulme_Counter.append(Block1Loop.thisRepN)
        
        # When Block Loop ends based on stimuli total
        if len(Block_Loop_Voulme_Counter) == 72: 
            volume_counter = 1 # Reset volume_counter
            Block_Loop_Voulme_Counter = [] # Reinitalize counter
            Block_1_Run_1_Started = False # Block 1 Run 1 finished
            Encoding_Started = True # Start of encoding for next block 
            Recognition_Started = False # End of recognition for next block
            Block_2_Run_2_Started = True # Begin next block DELETE?
            
        
        
        # check responses
        if recogTrialTestKeyRespRun1.keys in ['', [], None]:  # No response was made
            recogTrialTestKeyRespRun1.keys = None
        recognitionLoop_Block1Run1.addData('recogTrialTestKeyRespRun1.keys',recogTrialTestKeyRespRun1.keys)
        if recogTrialTestKeyRespRun1.keys != None:  # we had a response
            recognitionLoop_Block1Run1.addData('recogTrialTestKeyRespRun1.rt', recogTrialTestKeyRespRun1.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-9.000000)
        thisExp.nextEntry()
        
    # completed 12.0 repeats of 'recognitionLoop_Block1Run1'
    
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'Block1Loop'


# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
