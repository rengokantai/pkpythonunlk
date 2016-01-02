__author__ = 'Hernan Y.Ke'

from memory_profiler import profile

@profile(precision=4)
def profiletest():
    l1 = []
    for i in (1,100):
        l1.append(i)
    return l1
if __name__ == '__main__':
    profiletest()