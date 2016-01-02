__author__ = 'Hernan Y.Ke'

def run_com(*list_of_anim):
    if len(list_of_anim)<1:
        print("Nothing")
        return
    fatest_anim = list_of_anim[0]
    maxspeed = fatest_anim.running_speed()
    for anim in list_of_anim[1:]:
        runspeed = anim.running_speed()
        if runspeed > maxspeed:
            fatest_anim = anim
            maxspeed = anim.runspeed
    print("{}{}".format(fatest_anim.name,maxspeed))


class Cat(object):
    def __init__(self,name,legs):
        self.name=name
        self.legs=legs

    def running_speed(self):
        if self.legs > 4:
            return 20
        else:
            return 30

class Fish(object):

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def swim_speed(self):
        if self.age>1:
            return 20
        else:
            return 10

class RunningFish(object):

    def __init__(self,fish):
        self.legs=4
        self.fish=fish

    def running_speed(self):
        return self.fish.swim_speed()

    def __getattr__(self, item):
        return getattr(self.fish,item)

run_com(Cat('a',3),RunningFish(Fish('b',5)))