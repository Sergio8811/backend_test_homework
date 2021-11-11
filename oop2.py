from dataclasses import dataclass
@dataclass
class Transport:
    title: str
    price: int
    engine: any

class Engine:
    def __init__(self, power, title):
        self.power = power
        self.title = title
        
class Car:
    def __init__(self, title, color, price, engine: Engine):
        self.title = title
        self.color = color
        self.price = price
        self.engine = engine

    def show_price(self):
        print(f'Это машина марки {self.title}, она стоит {self.price}')
        print(f'Машина оборудована двигателем {self.engine.title} с мощностью {self.engine.power} л. с.')

class Track:
    def __init__(self, title, price, engine: Engine, bucket_volume):
        self.title = title        
        self.price = price
        self.engine = engine
        self.bucket_volume = bucket_volume

class Bike(Transport):
    def __init__(self, title, price, engine: Engine, sound):
        super().__init__(title, price, engine)
        self.sound = sound

    def get_sound(self):
        print(f'Мотоцикл марки {self.title} делает {self.sound}')

class Buyer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def car_buying(self, car: Transport):
        if self.balance < car.price:
            insufficient_funds = car.price - self.balance
            print(f'{self.name}, not enough money: {insufficient_funds}')
        else:
            self.balance -= car.price
            print(f'{self.name}, congrats! This car is yours!')

if __name__ == '__main__':
    engine_for_volvo60 = Engine(200, 'D420')
    engine_for_volvo90 = Engine(270, 'D520')
    first_car = Car('Volvo XC60', 'Белый', 6500000, engine_for_volvo60)
    second_car = Car('Volvo XC90', 'Черный', 7500000, engine_for_volvo90)
    first_buyer = Buyer('Георгий', 1500000)
    second_buyer = Buyer('Василий', 10000000)
    #first_car.show_price()
    #second_car.show_price()
    #print(second_buyer.balance)
    #second_buyer.car_buying(first_car)
    #print(second_buyer.balance)
    super_bike = Bike('Yamaha', 500000, engine_for_volvo90, 'вжжужужжуж')
    #super_bike.car_buying()
    first_buyer.car_buying(super_bike)
        