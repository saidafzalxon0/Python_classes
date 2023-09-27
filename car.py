class Car:
    brand='Chevralet'
    logo='plus'
    tezlik=250
    made_in='Uzbekistan'


class Car2(Car):
    def __init__(self, yoqilgi, rang, ot_kuchi, ):
        self.yoqilgi = yoqilgi
        self.rang = rang
        self.ot_kuchi = ot_kuchi
    def chiqar(self):
        print(self.brand,self.logo,self.tezlik,self.made_in,self.yoqilgi,self.rang,self.ot_kuchi)


class Car3 (Car):
    yoqilgi="elektr"
    def __init__ (self, marka):
        self.marka=marka

    def chiqar(self):
        print(self.brand, self.logo, self.tezlik, self.made_in, self.yoqilgi,self.marka)
car2 =Car2("benzin","oq",760)
car3 =Car3("laseti")
car2.chiqar()
car3.chiqar()