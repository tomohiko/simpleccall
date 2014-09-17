import commands
import sys
import ctypes


def compile(c_prog):
	fp = open(".temp.c", "w")
	fp.write(c_prog)
	fp.close()

	###"----gcc-----"
	ret = commands.getoutput("gcc -shared -lm -fPIC .temp.c -o .libtemp.so")

	if len(ret) != 0:
		print "Compile Error"
		print ret
		sys.exit(1)
	else:
		return 0

def load():
	####loading shared library###
	libtemp = ctypes.cdll.LoadLibrary("./.libtemp.so")
	return libtemp

