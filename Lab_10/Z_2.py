class Firm:
    def __init__(self, name_firm, founded):
        self.name_firm = name_firm
        self.founded = list(map(lambda el: int(el), founded.split(sep='.')))
        self.services = {}
        self.addresses_filial = {}

    def years_existence(self, years):
        years = list(map(lambda el: int(el), years.split(sep='.')))
        years_2 = (years[1] - self.founded[1]) * 365
        years_2 += (years[0] - self.founded[0]) * 30
        years_2 /= 365
        return int(years_2)


    def services_firm(self):
        self.services["services_name"] = input("Назва послуг: ")
        self.services["cost"] = input("Вартість: ")
        self.services["street"] = input("Термін виконання: ").split('.')
        return self.services

    def addresses_filial_firm(self):
        self.addresses_filial = {}
        self.addresses_filial["country"] = input("Країна: ")
        self.addresses_filial["city"] = input("Місто: ")
        self.addresses_filial["street"] = input("Вулиця: ")
        self.addresses_filial["house_number"] = input("Номер будинку: ")
        return self.addresses_filial

    def input_services(self):
        n = int(input("Кількість послуг: "))
        return [self.services_firm() for i in range(n)]

    def input_addresses_filial(self):
        m = int(input("Кількість філіалів: "))
        return [self.addresses_filial_firm() for i in range(m)]

    def search_addresses_filial(self, addresses_filial_title, list_addresses_filial):
        return list(filter(lambda addresses_filial:  self.addresses_filial["city"] == addresses_filial_title, list_addresses_filial))



firm = Firm("Intel", "6.1987")
print(firm.years_existence("12.2021"))
list_addresses_filial = firm.input_addresses_filial()
while True:
    ans = input('Do you want to search {y/n}?')
    if ans == 'n':
        break
    addresses_filial_title = input("Назва міста:")
    filial = firm.search_addresses_filial(list_addresses_filial, list_addresses_filial)
    if len(filial) > 0:
        print(filial)
    else:
        print("Нема філіалів")
