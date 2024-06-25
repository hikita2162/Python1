from smartphone import Smartphone

catalog = []
phone1 = Smartphone("POCO","C65","+79917474293")
phone2 = Smartphone("Redmi","Note 13 Pro+","+79968524499")
phone3 = Smartphone("infinix","note30","+79504538197")
phone4 = Smartphone("Honor","Magic V2","+79016480913")
phone5 = Smartphone("iPhone","15 Pro Max","+79029544953")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.Stamp} - {phone.Model}, {phone.Numder}")