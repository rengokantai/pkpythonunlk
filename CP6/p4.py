__author__ = 'Hernan Y.Ke'
import time
import _thread

def foo(t):
    print(time.time())
    time.sleep(t)
    print("done")
    print(time.time())

_thread.start_new_thread(foo,(3,))
_thread.exit_thread()