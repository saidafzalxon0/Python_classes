class Uy:
    xonalar = 5
    vanna = 2

class modern_uy(Uy):
    kamera = True
    wifi = True
    lift = True
    parking = True
    def __init__(self, etaj):
        self.etaj = etaj
    def farqi(self):
        print("Xonalar soni", self.xonalar,"Vannalar soni", self.vanna, "Etajlar soni", self.etaj,"Kamera", self.kamera,"Wifi", self.wifi, "Lift", self.lift, "Parking", self.parking)
modern_uy = modern_uy("45")
modern_uy.farqi()


