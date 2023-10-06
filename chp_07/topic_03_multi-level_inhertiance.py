class GrandFather:
    def skin_color(self):
        print("Sking color is White")
    def property(self):
        print("4 MARLA PROPERTY")
class Father(GrandFather):
    def heigth(self):
        print("Heigth is 5.11 ft")
    def vehicle(self):
        print("Car")
class Son(Father):
    def govt_job(self):
        print("Govt job")
    def anger_issue(self):
        print("I have ANGER issues")
# creating an object
print("Son .................")
ss = Son()
ss.skin_color()
ss.property()
ss.heigth()
ss.vehicle()
ss.govt_job()
ss.anger_issue()
# creating an object for father
print("Father .................")
ff = Father()
ff.skin_color()
ff.property()
ff.heigth()
ff.vehicle()
# creating an object for GrandFather
print("GRANDFATHER .................")
gg = GrandFather()
gg.property()
gg.skin_color()