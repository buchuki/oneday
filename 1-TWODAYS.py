#!/usr/bin/python3
from todo.utils import open_consecutive
import sys

try:
    if len(sys.argv) > 1:
        open_consecutive(int(sys.argv[1]))
    else:
        open_consecutive()
except ValueError:
    print("Argument must be an integer")
