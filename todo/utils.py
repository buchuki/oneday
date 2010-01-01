import datetime
import subprocess
import os
from .config import EDITOR

def open_day(num_days=0):
    day = datetime.date.today() + datetime.timedelta(num_days)
    day = day.strftime("%Y-%m-%d")
    subprocess.call("%s %s" % (EDITOR, day), shell=True)
