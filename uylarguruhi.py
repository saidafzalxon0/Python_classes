<<<<<<< HEAD
class Uy:
    xonalar = 5
    vanna = 2
class etaj2uy(Uy):
    etaj = "2 etaj uy"
    zvanok = "clock"
    xonalar = 10
    vanna = 5
    def tasvirla(self):
        print("Etaj:",self.etaj,"  Xonalar:",self.xonalar,"  Vanna:",self.vanna,"  Zvanok:",self.zvanok)

etaj2uy = etaj2uy()
etaj2uy.tasvirla()


class Orta(Uy):
      qavat = 5
      zvanok = True
      issiqsuv = True
      telefon = True

      def tasvirla (self):
           print("Qavatlar soni:",self.qavat,"Xonalar soni:", self.xonalar, "Vannalar soni", self.vanna, "Zvanok:", self.zvanok, "Issiqsuv:", self.issiqsuv, "Damashniy:", self.telefon)


Orta = Orta()
Orta.tasvirla()
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

