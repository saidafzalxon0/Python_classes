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
asus = Asus()
hp = Hp()

asus.tasvirla()
print("---------------------------------------------------------------------------------------------------------------------")
hp.tasvirla()