#!/usr/local/bin/python3
import subprocess

while(True):
	lines = ""
	with open("links.txt", "r") as f:
		lines = f.readlines()
	subprocess.check_output(['open', lines[0]])
	action = input("d for done: \n")
	if action=="d":
		with open("links.txt", "w") as f:
			f.write(''.join(lines[1:]))
	elif action=="q":
		break