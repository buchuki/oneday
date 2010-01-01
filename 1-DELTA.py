#!/usr/bin/python3
from todo.utils import open_day
import sys

try:
    open_day(int(sys.argv[1]))
except ValueError:
    print("Argument must be an integer")
except IndexError:
    print("Please specify the number of days from today")
