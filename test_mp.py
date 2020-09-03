import time

def sqr(num):
	print(num*num)
	return (num*num)

def f(a_list):
    out = 0
    for n in a_list:
        out += n*n
        time.sleep(0.1) 
    return out

def worker(x):
    return x*x