import os
import glob
import sys
import re

print(os.getcwd())      # Return the current working directory
print(os.system('mkdir today'))   # Run the command mkdir in the system shell
print(dir(os))
print(help(os))

print(glob.glob('*.py'))

print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')

re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

'tea for too'.replace('too', 'two')