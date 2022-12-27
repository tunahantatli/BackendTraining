class User:
    # yapıcı method (constructor)
    def __init__(self, username, password, email, name, age):
        # object attribute, instance attribute
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.age = age
    #instance method (yani objeye yönelik method)
    def info(self):
        return f"Sayın {self.name}, {self.username} kullanıcı adıyla sisteme başarıyla kaydoldunuz!"


u1 = User("tnhnttli", "123456789254", "tt@example.com", "Tunahan Tatlı", 25)
u2 = User("alpine", "fernandoAlonso_wentTo-astonmartinF1", "alpineF1@mail.com", "Alpine F1 Team", 1)
print(u1.username, u1.password, u1.email, u1.name, u1.age)
print(u2.username, u2.password, u2.email, u2.name, u2.age)
print(u1.info())
print(u2.info())
