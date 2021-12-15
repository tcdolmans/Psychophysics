#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on December 01, 2021, at 15:14
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'cueing'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'ExpData/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\SKIKK\\Documents\\1. Human Neuroscience\\1. Year 1\\Sem 1\\Psychophysics\\Own Experiment\\cueing_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1707, 960], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_text = visual.TextStim(win=win, name='intro_text',
    text='Dear Participant,\n\nThank you for taking part in this experiment. The objective of this experiment is to identify the effect of endogenous versus exogenous cues on both reaction time and signal detection. \n\nA ‘cue’ is an indication about which side the stimulus will appear on. These cues can be correct or incorrect. ‘Endogenous’ refers to a cue that one has to think about, in this case, an arrow pointing to one side. ‘Exogenous’ refers to a cue that is picked up by lower parts of the visual pathway, in this case, a flashing box. \n\nSometime after receiving your cue, a red dot will appear in the square on either side. The dot is quite dim, but it helps to keep looking at the fixation cross. Your task is to press the key that corresponds to the side of the stimulus (not the cue).\n\nIs it on the left? Press ‘a’. Is it on the right? Press ‘l’. Press them both once to get a feel for where they are.\n\nEverything clear? Press spacebar to continue. \n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
intro_resp = keyboard.Keyboard()

# Initialize components for Routine "endo_setcion"
endo_setcionClock = core.Clock()
key_resp = keyboard.Keyboard()
endo_right = visual.Rect(
    win=win, name='endo_right',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0.4, 0),
    lineWidth=25.0,     colorSpace='rgb',  lineColor='white', fillColor='0,0,0',
    opacity=None, depth=-1.0, interpolate=True)
endo_left = visual.Rect(
    win=win, name='endo_left',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(-0.4, 0),
    lineWidth=30.0,     colorSpace='rgb',  lineColor='black', fillColor='0, 0, 0',
    opacity=None, depth=-2.0, interpolate=True)
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
endo_cue = visual.ShapeStim(
    win=win, name='endo_cue',
    size=(0.02, 0.02), vertices='triangle',
    ori=1.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
endo_stimulus = visual.ShapeStim(
    win=win, name='endo_stimulus',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=0.01, depth=-5.0, interpolate=True)

# Initialize components for Routine "exo_section"
exo_sectionClock = core.Clock()
key_resp_2 = keyboard.Keyboard()
exo_right = visual.Rect(
    win=win, name='exo_right',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(0.4, 0),
    lineWidth=25.0,     colorSpace='rgb',  lineColor='black', fillColor='0.0000, 0.0000, 0.0000',
    opacity=None, depth=-1.0, interpolate=True)
exo_left = visual.Rect(
    win=win, name='exo_left',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=(-0.4, 0),
    lineWidth=25.0,     colorSpace='rgb',  lineColor='black', fillColor='0.0000, 0.0000, 0.0000',
    opacity=None, depth=-2.0, interpolate=True)
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.05, 0.05),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
exo_cue = visual.Rect(
    win=win, name='exo_cue',
    width=(0.3, 0.3)[0], height=(0.3, 0.3)[1],
    ori=0.0, pos=[0,0],
    lineWidth=30.0,     colorSpace='rgb',  lineColor='white', fillColor='0.0000, 0.0000, 0.0000',
    opacity=None, depth=-4.0, interpolate=True)
exo_stimulus = visual.ShapeStim(
    win=win, name='exo_stimulus',
    size=(0.15, 0.15), vertices='circle',
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=0.01, depth=-5.0, interpolate=True)

# Initialize components for Routine "outro"
outroClock = core.Clock()
outro_text = visual.TextStim(win=win, name='outro_text',
    text='Thank you for participating!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
intro_resp.keys = []
intro_resp.rt = []
_intro_resp_allKeys = []
intro_text.alignText = 'left'
# keep track of which components have finished
introComponents = [intro_text, intro_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        intro_text.setAutoDraw(True)
    if intro_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > intro_text.tStartRefresh + 500-frameTolerance:
            # keep track of stop time/frame for later
            intro_text.tStop = t  # not accounting for scr refresh
            intro_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(intro_text, 'tStopRefresh')  # time at next scr refresh
            intro_text.setAutoDraw(False)
    
    # *intro_resp* updates
    waitOnFlip = False
    if intro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_resp.frameNStart = frameN  # exact frame index
        intro_resp.tStart = t  # local t and not account for scr refresh
        intro_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_resp, 'tStartRefresh')  # time at next scr refresh
        intro_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(intro_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(intro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_resp.getKeys(keyList=['space'], waitRelease=False)
        _intro_resp_allKeys.extend(theseKeys)
        if len(_intro_resp_allKeys):
            intro_resp.keys = _intro_resp_allKeys[-1].name  # just the last key pressed
            intro_resp.rt = _intro_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro_text.started', intro_text.tStartRefresh)
thisExp.addData('intro_text.stopped', intro_text.tStopRefresh)
# check responses
if intro_resp.keys in ['', [], None]:  # No response was made
    intro_resp.keys = None
thisExp.addData('intro_resp.keys',intro_resp.keys)
if intro_resp.keys != None:  # we had a response
    thisExp.addData('intro_resp.rt', intro_resp.rt)
thisExp.addData('intro_resp.started', intro_resp.tStartRefresh)
thisExp.addData('intro_resp.stopped', intro_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('endo_cues.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "endo_setcion"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    endo_right.setLineColor('black')
    endo_cue.setPos(cue_position)
    endo_cue.setOri(cue_orientation)
    endo_stimulus.setPos(stim_position)
    # keep track of which components have finished
    endo_setcionComponents = [key_resp, endo_right, endo_left, fixation_cross, endo_cue, endo_stimulus]
    for thisComponent in endo_setcionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    endo_setcionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "endo_setcion"-------
    while continueRoutine:
        # get current time
        t = endo_setcionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=endo_setcionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= cue_time + 2-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['a', 'l'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *endo_right* updates
        if endo_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endo_right.frameNStart = frameN  # exact frame index
            endo_right.tStart = t  # local t and not account for scr refresh
            endo_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endo_right, 'tStartRefresh')  # time at next scr refresh
            endo_right.setAutoDraw(True)
        if endo_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endo_right.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                endo_right.tStop = t  # not accounting for scr refresh
                endo_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(endo_right, 'tStopRefresh')  # time at next scr refresh
                endo_right.setAutoDraw(False)
        
        # *endo_left* updates
        if endo_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endo_left.frameNStart = frameN  # exact frame index
            endo_left.tStart = t  # local t and not account for scr refresh
            endo_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endo_left, 'tStartRefresh')  # time at next scr refresh
            endo_left.setAutoDraw(True)
        if endo_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endo_left.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                endo_left.tStop = t  # not accounting for scr refresh
                endo_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(endo_left, 'tStopRefresh')  # time at next scr refresh
                endo_left.setAutoDraw(False)
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(False)
        
        # *endo_cue* updates
        if endo_cue.status == NOT_STARTED and tThisFlip >= cue_time + 1.5-frameTolerance:
            # keep track of start time/frame for later
            endo_cue.frameNStart = frameN  # exact frame index
            endo_cue.tStart = t  # local t and not account for scr refresh
            endo_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endo_cue, 'tStartRefresh')  # time at next scr refresh
            endo_cue.setAutoDraw(True)
        if endo_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endo_cue.tStartRefresh + .75-frameTolerance:
                # keep track of stop time/frame for later
                endo_cue.tStop = t  # not accounting for scr refresh
                endo_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(endo_cue, 'tStopRefresh')  # time at next scr refresh
                endo_cue.setAutoDraw(False)
        
        # *endo_stimulus* updates
        if endo_stimulus.status == NOT_STARTED and tThisFlip >= cue_time + 2-frameTolerance:
            # keep track of start time/frame for later
            endo_stimulus.frameNStart = frameN  # exact frame index
            endo_stimulus.tStart = t  # local t and not account for scr refresh
            endo_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endo_stimulus, 'tStartRefresh')  # time at next scr refresh
            endo_stimulus.setAutoDraw(True)
        if endo_stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > endo_stimulus.tStartRefresh + .1-frameTolerance:
                # keep track of stop time/frame for later
                endo_stimulus.tStop = t  # not accounting for scr refresh
                endo_stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(endo_stimulus, 'tStopRefresh')  # time at next scr refresh
                endo_stimulus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endo_setcionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "endo_setcion"-------
    for thisComponent in endo_setcionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    trials.addData('endo_right.started', endo_right.tStartRefresh)
    trials.addData('endo_right.stopped', endo_right.tStopRefresh)
    trials.addData('endo_left.started', endo_left.tStartRefresh)
    trials.addData('endo_left.stopped', endo_left.tStopRefresh)
    trials.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    trials.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    trials.addData('endo_cue.started', endo_cue.tStartRefresh)
    trials.addData('endo_cue.stopped', endo_cue.tStopRefresh)
    trials.addData('endo_stimulus.started', endo_stimulus.tStartRefresh)
    trials.addData('endo_stimulus.stopped', endo_stimulus.tStopRefresh)
    # the Routine "endo_setcion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
trials.saveAsText(filename + 'trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
exo_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exo_cues.xlsx'),
    seed=None, name='exo_trials')
thisExp.addLoop(exo_trials)  # add the loop to the experiment
thisExo_trial = exo_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExo_trial.rgb)
if thisExo_trial != None:
    for paramName in thisExo_trial:
        exec('{} = thisExo_trial[paramName]'.format(paramName))

for thisExo_trial in exo_trials:
    currentLoop = exo_trials
    # abbreviate parameter names if possible (e.g. rgb = thisExo_trial.rgb)
    if thisExo_trial != None:
        for paramName in thisExo_trial:
            exec('{} = thisExo_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "exo_section"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    exo_cue.setPos(cue_position)
    exo_stimulus.setPos(stim_position)
    # keep track of which components have finished
    exo_sectionComponents = [key_resp_2, exo_right, exo_left, fixation, exo_cue, exo_stimulus]
    for thisComponent in exo_sectionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    exo_sectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "exo_section"-------
    while continueRoutine:
        # get current time
        t = exo_sectionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=exo_sectionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= cue_time + 1.6-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['a', 'l'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *exo_right* updates
        if exo_right.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exo_right.frameNStart = frameN  # exact frame index
            exo_right.tStart = t  # local t and not account for scr refresh
            exo_right.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exo_right, 'tStartRefresh')  # time at next scr refresh
            exo_right.setAutoDraw(True)
        if exo_right.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > exo_right.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                exo_right.tStop = t  # not accounting for scr refresh
                exo_right.frameNStop = frameN  # exact frame index
                win.timeOnFlip(exo_right, 'tStopRefresh')  # time at next scr refresh
                exo_right.setAutoDraw(False)
        
        # *exo_left* updates
        if exo_left.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exo_left.frameNStart = frameN  # exact frame index
            exo_left.tStart = t  # local t and not account for scr refresh
            exo_left.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exo_left, 'tStartRefresh')  # time at next scr refresh
            exo_left.setAutoDraw(True)
        if exo_left.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > exo_left.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                exo_left.tStop = t  # not accounting for scr refresh
                exo_left.frameNStop = frameN  # exact frame index
                win.timeOnFlip(exo_left, 'tStopRefresh')  # time at next scr refresh
                exo_left.setAutoDraw(False)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # *exo_cue* updates
        if exo_cue.status == NOT_STARTED and tThisFlip >= cue_time + 1.5-frameTolerance:
            # keep track of start time/frame for later
            exo_cue.frameNStart = frameN  # exact frame index
            exo_cue.tStart = t  # local t and not account for scr refresh
            exo_cue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exo_cue, 'tStartRefresh')  # time at next scr refresh
            exo_cue.setAutoDraw(True)
        if exo_cue.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > exo_cue.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                exo_cue.tStop = t  # not accounting for scr refresh
                exo_cue.frameNStop = frameN  # exact frame index
                win.timeOnFlip(exo_cue, 'tStopRefresh')  # time at next scr refresh
                exo_cue.setAutoDraw(False)
        
        # *exo_stimulus* updates
        if exo_stimulus.status == NOT_STARTED and tThisFlip >= cue_time + 1.6-frameTolerance:
            # keep track of start time/frame for later
            exo_stimulus.frameNStart = frameN  # exact frame index
            exo_stimulus.tStart = t  # local t and not account for scr refresh
            exo_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exo_stimulus, 'tStartRefresh')  # time at next scr refresh
            exo_stimulus.setAutoDraw(True)
        if exo_stimulus.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > exo_stimulus.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                exo_stimulus.tStop = t  # not accounting for scr refresh
                exo_stimulus.frameNStop = frameN  # exact frame index
                win.timeOnFlip(exo_stimulus, 'tStopRefresh')  # time at next scr refresh
                exo_stimulus.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exo_sectionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "exo_section"-------
    for thisComponent in exo_sectionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    exo_trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        exo_trials.addData('key_resp_2.rt', key_resp_2.rt)
    exo_trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    exo_trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    exo_trials.addData('exo_right.started', exo_right.tStartRefresh)
    exo_trials.addData('exo_right.stopped', exo_right.tStopRefresh)
    exo_trials.addData('exo_left.started', exo_left.tStartRefresh)
    exo_trials.addData('exo_left.stopped', exo_left.tStopRefresh)
    exo_trials.addData('fixation.started', fixation.tStartRefresh)
    exo_trials.addData('fixation.stopped', fixation.tStopRefresh)
    exo_trials.addData('exo_cue.started', exo_cue.tStartRefresh)
    exo_trials.addData('exo_cue.stopped', exo_cue.tStopRefresh)
    exo_trials.addData('exo_stimulus.started', exo_stimulus.tStartRefresh)
    exo_trials.addData('exo_stimulus.stopped', exo_stimulus.tStopRefresh)
    # the Routine "exo_section" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'exo_trials'

# get names of stimulus parameters
if exo_trials.trialList in ([], [None], None):
    params = []
else:
    params = exo_trials.trialList[0].keys()
# save data for this loop
exo_trials.saveAsExcel(filename + '.xlsx', sheetName='exo_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
exo_trials.saveAsText(filename + 'exo_trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "outro"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
outroComponents = [outro_text]
for thisComponent in outroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
outroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "outro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = outroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=outroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *outro_text* updates
    if outro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        outro_text.frameNStart = frameN  # exact frame index
        outro_text.tStart = t  # local t and not account for scr refresh
        outro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(outro_text, 'tStartRefresh')  # time at next scr refresh
        outro_text.setAutoDraw(True)
    if outro_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > outro_text.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            outro_text.tStop = t  # not accounting for scr refresh
            outro_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(outro_text, 'tStopRefresh')  # time at next scr refresh
            outro_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "outro"-------
for thisComponent in outroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('outro_text.started', outro_text.tStartRefresh)
thisExp.addData('outro_text.stopped', outro_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
