class Car:
    pass

print("-------------------- Car ----------------------")

ford = Car()  # () is necessary to create the object and ford is the instance/object of the class Car
honda = Car()

ford.speed = 200  # we can assign to attributes on the fly
honda.speed = 220

ford.color = 'red'
honda.color = 'blue'

print(ford.speed)
print(honda.color)


# ------------------------------------------

class car02:
    def __init__(self, speed, color):  # it serves/behaves as/like constructor, but its not a constructor
        # you can not define multiple init methods. Even if you define the last one is valid, i.e the last init method iverrides the init method defined before
        self.speed = speed
        self.color = color
        self.number = 342583 # can define some static values, just to show not everything can be received as argument
        print(speed, color, self.number)

print("-------------------- car02 ----------------------")

ford02 = car02('red', 200)
honda02 = car02('blue', 220)

ford02.speed = 320
print(ford02.speed)

# ------------------------------------------

class car02a:
    def __init__(self, speed, color):  # it serves/behaves as/like constructor, but its not a constructor
        # you can not define multiple init methods. Even if you define the last one is valid, i.e the last init method iverrides the init method defined before
        self.speed = speed
        self.color = color
        self.number = 342583 # can define some static values, just to show not everything can be received as argument
        print(speed, color, self.number)

    def set_speed(self, value):
        self.speed = value

    def get_speed(self):
        return self.speed

print("-------------------- car02a ----------------------")
ford02a = car02a('red', 200)
honda02a = car02a('blue', 220)

ford02a.speed = 320
print(ford02a.speed)

ford02a.set_speed(330)
print(ford02a.get_speed())

# ------------------------------------------
# you don'' want to change some of the attributes of class, so encapsulation comes in picture, you can make your class attributes as private using __
# there is no explicit keyword to declare a variable as private
class car02b:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color
        print(speed, color)

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def __private_method(self):
        print("Its a private method")

print("-------------------- car02b ----------------------")
ford02b = car02b('red', 200)
honda02b = car02b('blue', 220)

ford02b.speed = 320
print(ford02b.speed)

ford02b.set_speed(330)
print(ford02b.get_speed())

ford02b.speed = 340 # now you can not assign value like this as it is declared as private
# print(ford02b.__speed) # AttributeError: 'car02b' object has no attribute '__speed', you can't access private members outside the class, you can use it directly only inside the class. And you can define the methods inside the class which can modify/operate on the private member variables
print(ford02b.get_speed())

# ford02b.__private_method() # can not use the private method outside the class
# ------------------------------------------

class car03:
    def __init__(self, *args):  # variable length arguments
        print(args[0], args[1])
        for arg in args:
            print(arg)


# you can not define multiple init methods. Even if you define the last one is valid, i.e the last init method iverrides the init method defined before
# self.speed = speed
# self.color = color
# print(speed, color)
print("-------------------- car03 ----------------------")

ford03 = car03('red', 200)
honda03 = car03('blue', 220)
# ------------------------------------------

class car04:
    def __init__(self, **kwargs):  # passing dictionary
        for k, v in kwargs.items():
            print(k, ' - ', v)


# you can not define multiple init methods. Even if you define the last one is valid, i.e the last init method iverrides the init method defined before
# self.speed = speed
# self.color = color
# print(speed, color)
print("-------------------- car04 ----------------------")

ford04 = car04(color='red', speed=200)
honda04 = car04(color='blue', speed=220)