import os

####### EDITOR is the command to open the editor of your choice
# Use this to get the EDITOR from your environment:
# EDITOR = os.environ.get('EDITOR', 'gvim')
EDITOR = "gvim"

###### A command to pass to your editor to open two files.
# Leave it blank if your editor just needs two files on one command line
# Use -O to open vim/gvim in a vertical split
# Use -p to open vim/gvim in multiple tabs
SPLIT_OPT = "-O"
