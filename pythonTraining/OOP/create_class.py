"""
class Car:
    pass

car1 = Car()
car2 = Car()
print(Car)
print(car1)
print(car2)

class Products:
    pass
p1 = Products() # macbook air
p2 = Products() # hp pavilion
p3 = Products() # asus zenbook

listProducts = [p1, p2, p3]
for p in listProducts:
    print(p)
    print(type(p))
"""


# yukarıda "" yorum olan bölümde sınıf oluşturmayı öğrendik


# Aşağıdaki bölümde de init metodunu kullanmayı öğreneceğiz :)
"""
class Urunler:
    def __init__(self):  # yapıcı method(constructor)
        self.name = "Mercedes C200"
        self.price = "$ 20,000"
        print("Ürün nesnesi olşuturuldu!")

urun_1 = Urunler()
urun_2 = Urunler()

print(urun_1.name, urun_2.name, urun_1.price)
"""
# yukarıda urun_1 ve urun_2 nin farklı nesneler olmasını istiyoruz ama aynı sonuçları alıyoruz!
# Bu tercih edilen bir kullanım şekli değil :) Adım Adım ilerleyelim


# Adım 1, name ve price parametrelerini belirttim.
# yani her ürün için self parametresi name, price ve isActive parametresi oluşturduk.
# isActive'i ürün satışta mı sorusu için koydum ve default olarak true tanımladım.
class Urunler:
    def __init__(self, name, price, isActive=True):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("Ürün nesnesi olşuturuldu!")


# Adım 2 ürünleri tanımladım
# urun_1 = Urunler(name,price,isActive)
urun_1 = Urunler("Maserati Ghbili", "32,000.00 €")
# urun_2 = Urunler(name,price,isActive)
urun_2 = Urunler("Subaru XV", "44,000.00€")
# urun_3 = Urunler(name,price,isActive)
urun_3 = Urunler("Seat Ateca", "34,000.00€", False)
# eğer isActive = True ise belirtmeye gerek yok, False'u belirtsek yeterli


# Adım 3 çıktısını aldım
print(urun_1.name, urun_1.price, urun_1.isActive)
print(urun_2.name, urun_2.price, urun_2.isActive)
print(urun_3.name, urun_3.price, urun_3.isActive)
"""
önemli!!!!!!!!
__init__() fonksiyonunda self parametresi bu örnekte bizim ürünümüzü temsil ediyor.
ürünümüz ne bir otomobil,
adı yani markasını name,
fiyatını price,
satışta olup olmadığını isActive ile gördük.
 self'in ne olduğunu asla unutmuyoruz! Self Önemli 
"""