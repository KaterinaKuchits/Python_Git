# 4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
# класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
# приём оргтехники на склад и передачу в определённое подразделение компании. Для
# хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.



class Storehaus:
    storehaus = {"printer": [], "scanner": [], "xerox": []}

    def __init__(self, address):
        self.address = address

    @staticmethod
    def show_storehaus():
        print(f'На данный момент на складe имеются: \n{Storehaus.storehaus}')


class Store(Storehaus):
    def trasfer_in_store(self, equipment, index):
        try:
            self.l = {equipment: Storehaus.storehaus[equipment].pop(index)}
            print(f'Оргтехника:{self.l}, перемещенна в магазин по адресу {self.address}.')
        except:
            print(
                f"Ошибка в методе trasfer_in_store:\nпервый параметр equipment = str(наименнование оргтехники)\nвторой параметр = int(индекс забераймой оргтехники со склада)!")

    def show_in_store(self):
        print(f'На данный момент в магазине, по адресу {self.address}, имеются: \n{Storehaus.storehaus}')


class Ofise_equipment(Storehaus):
    def __init__(self, address, year, brand):
        super().__init__(address)
        self.brand = brand
        self.year = year

    def transfer_storehaus(self, equipment):
        Storehaus.storehaus[equipment].append(self.__str__())

    def __str__(self):
        return f'Марка: {self.brand}, год: {self.year}'


class Printer(Ofise_equipment):
    pass


class Scanner(Ofise_equipment):
    pass


class Xerox(Ofise_equipment):
    pass

scanner_1 = Scanner("str.Lenina 23", "2020", "SCAN")
scanner_2 = Scanner("str.Lenina 23", "2000", "Canon")
printer_1 = Printer("str.Lenina 23", '2013', "Samsung")
xerox_1 = Xerox("str.Lenina 23", '2021', 'CanonPixma')

scanner_1.transfer_storehaus("scanner")
scanner_2.transfer_storehaus("scanner")
printer_1.transfer_storehaus("printer")
xerox_1.transfer_storehaus("xerox"),

Storehaus.show_storehaus()

my_store = Store("Дмитровское шоссе, дом 107")
my_store.trasfer_in_store("scanner", 1)
my_store.show_in_store()