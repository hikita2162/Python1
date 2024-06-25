class user:

    def __init__(self, first_name,last_name):
        print("я создался",first_name, last_name)
        self.firstname = first_name
        self.lastname = last_name 
        self.username = first_name, last_name

    def sayFirst_name(self):
        print("моё имя", self.firstname)

    def sayLast_name(self):
        print("моя фамилия",self.lastname)

    def sayUser_name(self):
        print("меня зовут", self.username)

user1 = user("Никита","догадин")  

