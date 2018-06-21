# Script Name   : create_dir_if_not_there.py
# Author        : Kumar Nitesh
# Created       : 21th June 2018
# Version       : 1.0
# Description   : Checks to see if a directory exists in the users home directory, if not then create it


import os		# Import the OS module

MESSAGE_TO_DISPLAY = 'The directory already exists, no need to create'

TEST_DIR_NAME = 'demodir'

try:
    home = os.path.expanduser('~')    # Set the variable home by expanding the user's set home directory
    print(home)   # Print the location

    if not os.path.exists(os.path.join(home, TEST_DIR_NAME)):    # os.path.join() for making a full path safely
        os.makedirs(os.path.join(home,TEST_DIR_NAME))       # If not create the directory, inside their home directory
    else:
        print(MESSAGE_TO_DISPLAY)

except Exception as e:
    print(e)