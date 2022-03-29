#coding=utf-8

def select_dir(dir_type):
	if dir_type=='asp':
		dir_path='./utils/ASP.txt'
	elif dir_type=='aspx':
		dir_path='./utils/ASPX.txt'
	elif dir_type=='jsp':
		dir_path='./utils/JSP.txt'
	elif dir_type=='php':
		dir_path='./utils/PHP.txt'
	else:
		print 'Wrong dir_type,only asp\\aspx\\jsp\\php.Please check and input again!'
		return -1
	return dir_path