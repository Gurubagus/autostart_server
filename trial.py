import psutil 
import os

program = 'firefox'

process_names = [proc.name() for proc in psutil.process_iter()]

if any(program in s for s in process_names):
	pass

else:
	print(program + ' not found')
	os.system("gpstart")