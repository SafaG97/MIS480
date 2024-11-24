class Automobile:
    vehicle_list = []
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
        Automobile.vehicle_list.append(self)

    @staticmethod
    def add_vehicle(vehicle):
        Automobile.vehicle_list.append(vehicle)

    @staticmethod
    def del_veh(vehicle_name):
        for vehicle in Automobile.vehicle_list:
            if vehicle.get_make()==vehicle_name:
                Automobile.vehicle_list.remove(vehicle)

    def del_vehicle(self):
        if self in Automobile.vehicle_list:
            Automobile.vehicle_list.remove(self)
            self = None
    def get_make(self):
        return self.__make


    def get_model(self):
        return self.__model


    def get_color(self):
        return self.__color


    def get_year(self):
        return self.__year


    def get_mileage(self):
        return self.__mileage


    def set_make(self, value):
        self.__make = value


    def set_model(self, value):
        self.__model = value


    def set_color(self, value):
        self.__color = value


    def set_year(self, value):
        self.__year = value


    def set_mileage(self, value):
        self.__mileage = value


    def __str__(self):
        return "vehicle make: " + self.get_make() + " model: " + str(
            self.get_model()) + " color: " + self.get_color() + " year: " + str(self.get_year()) + " mileage: " + str(
            self.get_mileage())
def menu():
    print("Enter choice")
    print("1. Add vehicle")
    print("2. Delete vehicle")
    print("3. update vehicle")
    print("4. exit")
    choice=input()
    return choice

def main():
    while True:
        choice=int(menu())
        if choice==1:
            print("Enter vehicle name")
            name=input()
            color=input("Enter vehicle color")
            year=input("Enter vehicle year")
            mileage=input("Enter vehicle mileage")
            model=input("Enter vehicle model")
            vehicle = Automobile(name, model, color, year, mileage)
        elif choice==2:
            name=input("Enter vehicle name")
            Automobile.del_veh(name)
        elif choice==3:
            print("Enter vehicle name")
            name = input()
            color = input("Enter vehicle color")
            year = input("Enter vehicle year")
            mileage = input("Enter vehicle mileage")
            model = input("Enter vehicle model")
            vehicle = Automobile(name, model, color, year, mileage)
        elif choice==4:
            break
        file = open("inventory.txt", "w")
        for v in Automobile.vehicle_list:
            file.write(str(v) + "\n")

main()
