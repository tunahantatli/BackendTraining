# Class Attributes (Sınıf Öznitelikleri)

# sınıfımızı tanımladık 
class User:
    # değişkeni aşağıda tanımlıyoruz
    active_users = 0
    def __init__(self, username,name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        # init() içerisinde kullanıcı oluşturduğumuz için aktif kullanıcı sayısını 1 arttıracağız.
        User.active_users +=1

    def userName(self):
        return f"{self.username}"
    
    def Logout(self):
        return f"{self.username} log out"
        User.active_users -=1

print(f"Aktif Kullanıcı Sayısı: {User.active_users}")
#kullanıcıları oluşturduk
user1= User("tnhn", "tunahan", "tatlı",25)
user2= User("Rmzn", "Ramazan", "tatlı",52)
user3= User("emsttl", "emiş", "tatlı",48)
user4= User("tyttl", "tayyo", "tatlı",23)


#   kişi oluşturulduğunda aktif kulanıcı sayısının bir artmasını 
#  kullanıcı çıktığında bir azalmasını istiyoruz. class'ın içinden 6. satıra bakalım :D 6yı yeniden düzenledik


print(f"Aktif Kullanıcı Sayısı: {User.active_users}")
