from core.color import red, blue, green, gray, yellow, rose, bl_cl, reset, error, skyblue
import os, argparse, sys
def banner():
	print (red)
	os.system("cat core/banner")
	print (gray+"\t\t\tcoded by @ansanbinoy")
#	print (yellow+"  [+] twitter.com/ansanbinoy\t\t[+] github.com/ansanbinoy")
	print (gray+"-----------------------------------------------------------------------"+reset)
def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--file",dest="file",help="Path of your subdomain list or urls list")
	parser.add_argument("-t","--threads",dest="thread",help="Set a threading cout default is is 10",required=False,default=10)
#	parser.add_argument("-s","--sort",dest="sort",help="You can sort http status code  [''2xx, 3xx, 4xx, 5xx or all'] ",required=False, default="all")
	parser.add_argument("-o","--output",dest="output",help="Define a output file its not requires", required=False, default=False)
	options = parser.parse_args()
	if not options.file:
		sys.exit(parser.print_help())
	else:
	 	return options
