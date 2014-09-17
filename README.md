simpleccall
===========

Simple C-Language Call Library from python.

###Usage
import SimpleC
c_prog = """
#include <stdio.h>

int add(int x, int y) {
	return x + y;
}
"""
SimpleC.compile(c_prog)
mylib = SimpleC.load()

result = mylib.add(7, 8)
print result

> 15

###SAMPLE
$python sample.py
