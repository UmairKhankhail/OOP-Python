class GrandFather():

    def locker1(self):
        print('Your can access locker 01.')

    def locker2(self):
        print('You can access locker 02.')

class Father():

    def locker3(self):
        print('you can access locker 03.')

    def locker4(self):
        print('you can access locker4')

class GrandSon(Father,GrandFather):
    def locker5(self):
        print('you can access locker5')

umair=GrandSon()
umair.locker5()
umair.locker1()
umair.locker2()
umair.locker4()