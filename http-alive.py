__author__ = 'ansanbinoy'
# [+] github.com/ansanbinoy
# [+] twitter.com/ansanbinoy
#importing modules

import requests, os, sys
from threading import Thread
import multiprocessing
from core.color import gray, red, blue, green, yellow, rose, reset, error, bl_cl, skyblue
from core.requestor import launch
from core.init import banner, get_arguments
#main function

def main():
	banner()
	args = get_arguments()
	file = args.file
	th = int(args.thread)
	output = args.output
	try:
		urls = open(file).read().splitlines()
	except FileNotFoundError:
		sys.exit(f'{error}{green}\'{file}\' File not found!.{reset}')
	launch(urls,th,output)
if __name__ == '__main__':
	main()
