class Computer:
        klaviatura = "qwert"
        rangi = "Kulrang"
        toshi = "intel core-i5"

class Asus(Computer):
    model = "Asus"
    narxi = 500

    def tasvirla(self):
        print("Model:", self.model, "Narxi:", self.narxi, "Klaviatura:", self.klaviatura, "Rangi:", self.rangi, "Toshi:", self.toshi)

class Hp(Computer):
    model = "Hp"
    narxi = 550
    atpechatka = True

    def tasvirla(self):
         print("Model:", self.model, "Narxi:", self.narxi, "Atpechatka", self.atpechatka, "Klaviatura:", self.klaviatura, "Rangi:", self.rangi, "Toshi:", self.toshi)

class Acer(Computer):
    ovoz=100
    ssd=256
    aparativka=8

    def tasvirla(self):
        print("klavatura",self.klaviatura,"rangi",self.rangi,"toshi",self.toshi, " ovoz",self.ovoz,"ssd",self.ssd,"aparativka",self.aparativka)

class Lenovo(Computer):
    sceern ="15.6 HD"
    yoruglik=100
    model="lenovo"

    def tasvirla(self):
        print("ekran",self.sceern,"yorug'lik",self.yoruglik,"model",self.model,"klavatura",self.klaviatura,"rangi",self.rangi,"toshi",self.toshi)

acer=Acer()
lenovo=Lenovo()


print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
lenovo.tasvirla()
asus = Asus()
hp = Hp()

asus.tasvirla()
print("---------------------------------------------------------------------------------------------------------------------")
hp.tasvirla()