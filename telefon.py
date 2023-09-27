class Telefon:
    ovoz = 100
    yoruglik = 100

class Iphone(Telefon):
    sistema = "iOS"
    internet = "5g"
    def __init__(self,rang) -> None:
        self.rang = rang
    def tasvirla(self):
        print("SYSTEM:", self.sistema,  "INTERNET:", self.internet,  "OVOZ:" ,self.ovoz,  "YORUG'LIK:", self.yoruglik)



Iphone = Iphone("gold")
Iphone.tasvirla()