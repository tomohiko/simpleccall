#!/usr/bin/python

import SimpleC
import ctypes

c_prog = """
#include <stdio.h>
#include <math.h>

int add(int x, int y) {
	return x + y;
}

double tax(int price, double rate){
	return price + price * rate;
}

char *msg(void){
	char* msg = "Hellow, World!!";
	return msg;
}

"""

SimpleC.compile(c_prog)
mylib = SimpleC.load()

###int
result = mylib.add(7, 8)
print result

###double
mylib.tax.restype = ctypes.c_double
mylib.tax.argtypes = [ctypes.c_int, ctypes.c_double]
result = mylib.tax(95, 0.05)
print result

###char pointer
mylib.msg.restype = ctypes.c_char_p
result = mylib.msg()
print result
