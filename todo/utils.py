import datetime
import subprocess
import os
from .config import EDITOR, SPLIT_OPT

def open_day(num_days=0):
    '''Open today, or the given number of days from today (negative
    values supported) in the configured editor.'''
    day = datetime.date.today() + datetime.timedelta(num_days)
    day = day.strftime("%Y-%m-%d")
    subprocess.call("%s %s" % (EDITOR, day), shell=True)

def open_consecutive(num_days=0):
    '''Open two consecutive days, starting with today or the given number of
    days from today in a split tab. Assumes split tabs are supported in the
    editor.'''
    day = datetime.date.today() + datetime.timedelta(num_days)
    day2 = day + datetime.timedelta(1)
    day = day.strftime("%Y-%m-%d")
    day2 = day2.strftime("%Y-%m-%d")
    subprocess.call("%s %s %s %s" % (EDITOR, SPLIT_OPT, day, day2), shell=True)
