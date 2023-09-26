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


class Car3 (Car):
    yoqilgi=elektr
    def __init__ (self, marka):
        self.marka=marka


