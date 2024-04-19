# Python Performance Modnitoring Module by Christian Ortiz v0.0
import time

def exacStart():
    startTime = time.time()
    return startTime

def exacStop():
    stopTime = time.time()
    return stopTime

def exacTime(startTime, stopTime):
    return f"Execution tim: {startTime - stopTime} seconds. \n"