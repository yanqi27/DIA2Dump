#!/usr/bin/env python

# This script finds pdb file that matches the input debug_identifier

import sys
import os
import subprocess

dia2dump_cmd = 'F:\\Projects\\Backtrace\\bin64\\dia2dump.exe'

def check_id(path, id):
	try:
		p1 = subprocess.Popen([dia2dump_cmd, '-id', path],
							stdout = subprocess.PIPE)
		output = p1.communicate()[0]
		lines = output.splitlines()
		for line in lines:
			tokens = line.split(',')
			if tokens[1] == id:
				return True
	except Exception as e:
		print(e)
		pass
	return False

def main(args):
	if len(args) != 2:
		sys.stderr.write('search_id.py <path> <debug_id>\n');
		sys.exit(0)
	path = args[0]
	id = args[1]
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith('.pdb'):
				filepath = os.path.join(root, name)
				if check_id(filepath, id):
					sys.stdout.write('%s\n' % filepath)
					sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])
