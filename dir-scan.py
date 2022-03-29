#coding=utf-8

from config import *
from common import *
import threading
import Queue
import sys
import requests
from optparse import OptionParser
class dir_scan(threading.Thread):
	def __init__(self,qeque,dir_size):
		threading.Thread.__init__(self)
		self.qeque=qeque
		self.dir_size=dir_size

	def run(self):
		while not self.qeque.empty():
			dir_path = self.qeque.get()
			res = requests.get(url + dir_path)
			if res.status_code == 200:
				sys.stdout.write('Find {}{}!'.format(url,dir_path))
			sys.stdout.write('\r Finish '+str((1-self.qeque.qsize()*1.0/self.dir_size)*100)+'%')
			sys.stdout.flush()


def main(dir_path,thread_count):
	task = Queue.Queue()
	thread_list = []
	dir_size = 0
	thread_count=int(thread_count)
	with open(dir_path) as dir_file:
		while True:
			line = dir_file.readline()
			if line:
				line = line.replace('\n', '')
				task.put(line)
				dir_size += 1
			else:
				break
	for i in xrange(thread_count):
		thread_list.append(dir_scan(task,dir_size))
	for i in xrange(thread_count):
		thread_list[i].start()
	for i in xrange(thread_count):
		thread_list[i].join()

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="dir_type",help="Type of dictionary used")
	parser.add_option("-t", "--thread", dest="thread_count", default=10,help="Number of threads")
	(options, args) = parser.parse_args()
	if options.dir_type:
		dir_path=select_dir(options.dir_type)
		if dir_path==-1:
			sys.exit()
	else:
		print 'Please input the dir_type!'
		sys.exit()
	print options.dir_type,options.thread_count
	main(dir_path,options.thread_count)