
class one:
    def show1(self):
        print("This is in class one")

class two(one):
    def show2(self):
        print("This is in class two")

obj=two()
obj.show1()
obj.show2()