#!/usr/bin/python
from todo import todo_utils
import sys

try:
    todo_utils.open_day(int(sys.argv[1]))
except ValueError:
    print("Argument must be an integer")
except IndexError:
    print("Please specify the number of days from today")
