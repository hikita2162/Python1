class User:

    def __init__(self, first_name,last_name):
        print("я создался",first_name, last_name)
        self.first_name = first_name
        self.last_name = last_name 
        self.user_name = first_name, last_name

    def sayFirst_name(self):
        print("моё имя", self.first_name)

    def sayLast_name(self):
        print("моя фамилия",self.last_name)

    def sayUser_name(self):
        print("меня зовут", self.user_name)

user1 = User("Никита","догадин")  




