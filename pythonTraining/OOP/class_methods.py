class User:
    active_users = 0

    @classmethod 
    def display_active_users(cls): 
        return f'Aktif Kullanıcı: {cls.active_users}'
        # yukarıdaki class method ile aktif kullanıcı sayısını aldık
    def __init__(self, username, name, surname, age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1
     
    # __init__ ile kullanıcı oluşturmuştuk. şimdi de class method ile kullanıcı oluşturalım
    @classmethod
    def from_str(cls, data_str):
        username,name,surname,age = data_str.split(',')
        return cls(username,name,surname,age)
    
    def userName(self):
        return f'{self.username}'
    
    def Logout(self):
        User.active_users -= 1
        return f'{self.username} logout system'

print(User.display_active_users())
# user1= User("tnhn", "tunahan", "tatlı",25)
# user2= User("Rmzn", "Ramazan", "tatlı",52)
# user3= User("emsttl", "emiş", "tatlı",48)
# user4= User("tyttl", "tayyo", "tatlı",23)



user5 = User.from_str("brhmkbb, İbrahim, Akbaba,26")
print(User.display_active_users())
print(user5.username)
print(user5.name)
print(user5.surname)
print(user5.age)