from Address import Address
from Mailing import Mailing

to_address = Address("14145", "Москва","беговая","12","238")
from_address = Address("10013", "Калуга","деревня хохловка","15","15")
Mailing = Mailing(to_address, from_address, 500,"AKA477")

print(f"Отпровление 0{Mailing.track} из {Mailing.from_address.index}, {Mailing.from_address.city},"
      f" {Mailing.from_address.street}, {Mailing.from_address.house} - {Mailing.from_address.apartment}"
      f" в {Mailing.from_address.index}, {Mailing.from_address.city}, {Mailing.from_address.street},"
      f" {Mailing.from_address.house} - {Mailing.from_address.apartment}. Стоймость {Mailing.cost} рублей.")