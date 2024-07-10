from Address import Address
from Mailing import Mailing

to_address = Address("14145", "Москва","беговая","12","238")
from_address = Address("10013", "Калуга","деревня хохловка","15","15")
Mailing = Mailing(to_address, from_address, 500,"AKA477")

print(f"Отпровление 0{mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment}"
      f" в {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street},"
      f" {mailing.from_address.house} - {mailing.from_address.apartment}. Стоймость {mailing.cost} рублей.")