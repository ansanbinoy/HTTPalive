import requests
import os
import threading
import sys
import argparse
import multiprocessing
os.system("clear")
S = "\033[90m"
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
multiprocessing.Process = threading.Thread
class Http(multiprocessing.Process):
	def __init__(self):
		global W
		W = "\033[0m"
		self.S = "\033[90m"
		self.R = "\033[91m"
		self.G = "\033[92m"
		self.Y = "\033[93m"
		self.B = "\033[94m"
		print (self.R)
		os.system("cat banner")
		print (self.S+"\t\t\tcoded by @ansanbinoy")
		print (self.Y+"  [+] twitter.com/ansanbinoy\t\t[+] github.com/ansanbinoy")
		print (self.S+"-----------------------------------------------------------------------"+W)
		multiprocessing.Process.__init__(self, target = self.main)
		parser = argparse.ArgumentParser()
		parser.add_argument("-f","--file",dest="file",help="Path of your subdomain list or urls list")
		parser.add_argument("-p","--protocol",dest="protocol",help="-f for which protocol os running the domain HTTP/HTTPS or your list have you specified the HTTP/HTTPS you do -f NA ",required=False, default="na")
		parser.add_argument("-s","--sort",dest="sort",help="You can sort http status code  [''2xx, 3xx, 4xx, 5xx or all'] ",required=False, default="all")
		parser.add_argument("-o","--output",dest="output",help="Define a output file its not requires", required=False, default=False)
		self.options = parser.parse_args()
		print (W)
		if not self.options.file:
			parser.print_help()

		self.pro = str(self.options.protocol.lower())
		self.out = []
		print (W)
	def check(self):
		global domains
		with open(self.options.file,"r") as domains:
			for i in domains:
				i = i.strip()
				if self.pro == "http" or self.pro == "https":
					url = self.options.protocol.lower()+"://"+i
					try :
						x = requests.get(url)
						code = str(x.status_code)
						if self.options.sort.lower() == "all":
							self.out.append(url+" -->"+code)
							if code[0] == "2":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.G+code)
							elif code[0] == "3":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.B+code)
							elif code[0] == "4":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.R+code)
							elif code[0] == "5":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.Y+code)
						elif self.options.sort.lower() == "2xx":
							if code[0] == "2":
								self.out.append(url+" -->"+code)
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t[+] "+self.G+code)
						elif self.options.sort.lower() == "3xx":
							if code[0] == "3":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t[+] "+self.B+code)
						elif self.options.sort.lower() == "4xx":
							if code[0] == "4":
								self.out.append(url+" -->"+code)
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t[+] "+self.R+code)
						elif self.options.sort.lower() == "5xx":
							if code[0] == "5":
								self.out.append(url+" -->"+code)
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t[+] "+self.Y+code)
					except KeyboardInterrupt:
						print (self.R+"Exiting ..")
						print (W)
						sys.exit()
					except :
						print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [~] "+self.R+"Url not found")
						self.out.append(url+" -->Failed to cennetct!!")
				elif self.pro == "na":
					url = i
					try :
						x = requests.get(url)
						code = str(x.status_code)
						if self.options.sort.lower() == "all":
							self.out.append(url+" -->"+code)
							if code[0] == "2":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.G+code)
							elif code[0] == "3":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.B+code)
							elif code[0] == "4":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.R+code)
							elif code[0] == "5":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.Y+code)
						elif self.options.sort.lower() == "2xx":
							if code[0] == "2":
								self.out.append(url+" -->"+code)
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.G+code)
						elif self.options.sort.lower() == "3xx":
							if code[0] == "3":
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.B+code)
						elif self.options.sort.lower() == "4xx":
							if code[0] == "4":
								self.out.append(url+" -->"+code)
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.R+code)
						elif self.options.sort.lower() == "5xx":
							if code[0] == "5":
								self.out.append(url+" -->"+code)
								print (self.B+"[+] "+self.G+url+self.B+"\t\t\t [+] "+self.Y+code)
					except KeyboardInterrupt :
						print (self.R+"Exiting ..")
						print (W)
						sys.exit()
					except :
						print (self.B+"[+] "+self.G+url+self.B+"\t\t\t[~] "+self.R+"Url not found!!")
						self.out.append(url+" -->Failed to cennetct!!")
	def output(self, filename, content):
		with open(filename,"w+") as out:
			for i in content:
				out.write(str(i+"\n"))
	def main(self):
		self.check()
		if not self.options.output:
			pass
		else:
			self.output(self.options.output, self.out)

try:
	x = Http()
	x.main()
except KeyboardInterrupt:
	print (R+"Exiting..")
	print (W)
	sys.exit()
except Exception as e:
	print (B+"[+] "+G+"python3 http-aliv.py -h")
	print ("Ex:")
	print (B+"[~] "+G+"python3 http-alive.py -f subdomain.txt -p http -s all")
	print (B+"[~] "+G+"python3 http-alive.py -f subdomain.txt -p https -s 2xx")
	print (B+"[~] "+G+"python3 http-alive.py -f subdomain.txt -p na")
	print (e)
print (W)

								
