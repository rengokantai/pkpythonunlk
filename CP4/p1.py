__author__ = 'Hernan Y.Ke'
def less_than(self, other):
    return self.data <= other.data

class My(object):

    def __init__(self,data):
        self.data = data

    def __str__(self):
        return str(self.data)

    __repr__ = __str__

if __name__ == '__main__':

    lis = [My(i) for i in range(10,5,-1)]
    try:
        lis.sort()
    except TypeError:
        print("error")

    for att in '__lt__','__le__','__gt__','__ge__':
        setattr(My,att,less_than)
