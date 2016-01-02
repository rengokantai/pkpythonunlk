__author__ = 'Hernan Y.Ke'

from datetime import datetime,timedelta
from functools import wraps
import time
import line_profiler

l = []
def func_a():
    global l
    for i in range(1000):
        l.append(i)

def func_b():
    m = list(range(1,1000))

def func_c():
    func_a()
    func_b()
    k=list(range(1000))

if __name__ == '__main__':
    profiler = line_profiler.LineProfiler()
    profiler.add_function(func_c)
    profiler.run('func_c()')
    profiler.print_stats()