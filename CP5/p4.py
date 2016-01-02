__author__ = 'Hernan Y.Ke'
class AlooDish(object):
    # Act as template
    def get_ingredients(self,):
        self.ingredients = {}

    def prepare_vegetables(self,):
        for item in self.ingredients.items():
            print("take {} {} and cut into smaller pieces".format(item[0],item[1]))
        print("cut all vegetables in small pieces")

    def fry(self,):
        print("fry for 5 minutes")

    def serve(self,):
        print("Dish is ready to be served")

    def cook(self,):
        self.get_ingredients()
        self.prepare_vegetables()
        self.fry()
        self.serve()

class AlooMatar(AlooDish):
    #subclasse
    def get_ingredients(self,):
        self.ingredients = {'aloo':"1 Kg",'matar':"1/2 kg"}

    def fry(self,):
        print("wait 10 min")

class AlooPyaz(AlooDish):
    #subclass
    def get_ingredients(self):
        self.ingredients = {'aloo':"1 Kg",'pyaz':"1/2 kg"}

aloomatar = AlooMatar()
aloopyaz = AlooPyaz()
print("*******************  aloomatar cook")
aloomatar.cook()
print("******************* aloopyaz cook")
aloopyaz.cook()