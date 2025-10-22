"""__init__"""

# Libraries
import os
import sys
import time

# Root directory
root_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
if root_dir not in sys.path:
    sys.path.append(root_dir)

# Variables
start_time = time.time()
