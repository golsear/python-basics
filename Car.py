class Car():
    def __init__(self, mileage, fuel):
        self.mileage = mileage 
        self.fuel = fuel

    def vitr(self): 
        self.fuel = self.fuel - 3
        print("залишилось пального " + str(self.fuel) + " л")
    
    def zapr(self): 
        self.fuel = self.fuel + 10
        print("заправляємо машину на " + str(self.fuel) + " л")

car1 = Car(0, 0)
print("Пробіг", car1.mileage)
car1.zapr()
a = int(input("відстань?"))

while (a>0):
    print("ЇДЕМО!")
    a = a - 50
    print("залишилось " + str(a) + " км")
    car1.vitr()
    if(car1.fuel < 3): car1.zapr()
print("ФІНІШ!")