__author__ = 'Hernan Y.Ke'
from datetime import datetime,timedelta
from functools import wraps
import time

def showtime(func):

    @wraps(func)
    def wrap(*args, **kwargs):
        starttime = time.time()
        result = func(*args, **kwargs)
        endtime = time.time()
        print("%s %s"%(func.__name__, endtime-starttime))

    return wrap

@showtime
def func_c():
    for i in range(1000):
        for j in range(1000):
            for k in range(100):
                pass
if __name__ == '__main__':
    func_c()