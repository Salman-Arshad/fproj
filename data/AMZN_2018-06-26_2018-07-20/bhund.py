import os
import subprocess

p = subprocess.Popen(['python', 'l.py'], stdout=subprocess.PIPE)
o = p.communicate()[0]
print(o)
