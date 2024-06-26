import os
import logging
import json
import re
from subprocess import call
from .ColorUtils import *

def printDecisionAndMigrations(decision, migrations):
	print('Decision: [', end='')
	for i, d in enumerate(decision):
		if d not in migrations: print(color.FAIL, end='')
		print(d, end='')
		if d not in migrations: print(color.ENDC, end='')
		print(',', end='') if i != len(decision)-1 else print(']')
	print()


def unixify(paths):
	for path in paths:
		for file in os.listdir(path):
			if '.py' in file or '.sh' in file:
				_ = os.system("bash -c \"dos2unix "+path+file+" 2&> /dev/null\"")

def splitOnPeriods(string):
    result = []
    current_segment = []
    
    for char in string:
        if char.isspace():
            break
        elif char == '.':
            if current_segment:
                result.append(''.join(current_segment))
                current_segment = []
        else:
            current_segment.append(char)
    
    if current_segment:
        result.append(''.join(current_segment))
    
    return result