
from bonanza import *
from Car_class import*
from electrical_car import*
from typing import ValuesView


def main(args):

    # list.........
    power_root()
    min_max_sum()
    compi_generator()
    sliced_list(["mahmoud", "ahmed", "omar", "jackob", "john"])
    copy_list()
    # list..........
    # tuple.........
    looping_tuple()
    # tuple..........
    # if_statment.....
    if_statment_demo(['mg', 'bmw', 'seat', 'renu', 'subaru'])
    mapping_multipleConditions(
        {'mahmoud': 33, 'ahmed': 18, 'ibrahim': 24, 'ali': 4})
    if_multiple_list()
    # if_statment.....
    # Dict............
    acess_dict()
    nested_dict()
    dict_inside_list()
    # Dict............
    # input...........
#    prompt = "Tell Us More About Your Self"
#    prompt += "\n Let's Start with Your First Name: "
#    print(input(prompt))
#    age=input("Can you tell us your age?? ")
#    print(int(age))
    # input..........
    # whileloops......
    # while_loop()
    # input_in_dict()
    user_info = full_name_profile('mahmoud', 'essam',             profeciency='devsecops', location='singapore')
    print(user_info)
    # class instances
    doges()
    electrical_car_states()
    return 0


#extracted class method instances
def doges():
    Dog
    my_dog = Dog('Rocky', '5')
    your_dog=Dog('willie',7)
    your_dog.Sit()
    your_dog.Roll_Over()
    my_dog.Sit()
    my_dog.Roll_Over()
def electrical_car_states():
    Electical_Car
    electical_Car= Electical_Car('tesla','r5','2020')
    electical_Car.get_descriptive_name()
    electical_Car.increment_odometer(miles=2000)
    electical_Car.describe_battery(90)
    electical_Car.get_range(85)
#extracted class method instances

# list........
def power_root(sqaures=[], square=None):
    for value in range(1, 11):
        square = value**2
        sqaures.append(square)
    print(sqaures)
    return sqaures


def min_max_sum(digits=list(range(10, 50))):
    mi = min(digits)
    print(f"the minimum number is: {mi}")
    maxi = max(digits)
    print(f"the maximum number is: {maxi}")
    sumi = sum(digits)
    print(f"the sum of numbers is: {sumi}")
    return digits


def compi_generator(geni=[value**2 for value in range(3, 20)]):
    print(geni)


def sliced_list(players=[]):
    print(players[0:3])
    print(players[:4])
    print(players[2:])
    for x_player in players[-3:]:
        print(x_player.title())


def copy_list():
    food = ['pizza', 'salat', 'cake', 'fries']
    copied_food = food[:]
    copied_food.append('rice')
    food.append('ice-cream')
    print(f'original list is {food}')
    print(f'copied list is {copied_food}')
# list.............

# tuple.............


def looping_tuple():
    dimension = (122, 344, 67788, 4333, 2344, 655)
    for x in dimension:
        print(x)
# tuple.............


# if_statment.....
def if_statment_demo(cars=[]):
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())
    return car


def mapping_multipleConditions(Ids={}):
    for i in Ids.values():
        if i >= 18:
            print(f'{i}')
        else:
            continue
    print(f'number of {i} entites searched')


def if_multiple_list():
    available_toppings = ['mushrooms', 'olives', 'green peppers',
                          'pepperoni', 'pineapple', 'extra cheese']
    requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping} ")
        else:
            print(f"Sorry, we don't have {requested_topping} ")
    print("\nFinished making your pizza!")
# if_statment......


# Dict.........
def acess_dict(laptops={}):
    laptops['lenovo'] = 'LenovoZenPad'
    laptops['dell'] = 'DellG5'
    laptops['hp'] = 'Hp Pavillion'
    laptops['msi'] = 'MSI Gre'
    print(laptops)
    del laptops['msi']
    print(laptops)
    for key, value in laptops.items():
        print(f'\n keys: {key}')
        print(f'value: {value}')
    return laptops


def nested_dict():
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}
    aliens = [alien_0, alien_1, alien_2]
    for alien in aliens:
        print(alien)


def dict_inside_list():
    num = []
    for x in range(5):
        color_num_ratio = {"red": 2, "yellow": 1,
                           "green": 5, "blue": 6,         "black": 10}
        num.append(color_num_ratio)
    print(num)
    for x in num[:2]:
        print(sorted(x))
        if x["green"] == 5 and x["yellow"] == 1:
            x["green"] = 15
            x["yellow"] = 20
    print(sorted(x.values()))
    print("-------")
# dict...........


# while_loop....
def while_loop(message=""):
    prompt = "\nTell me something, and I will repeat it back to you:"
    prompt += "\nEnter 'quit' to end the program. "
    while message != 'quit':
        message = input(prompt)
        if message == 'quit':
            break
        else:
            print(message)

    return message


def input_in_dict(credentials={}):
    active = True
    while active == True:
        username = input('\n input user name: ')
        ids = input('\n input user id:')
        credentials[username] = ids
        terminate = input('\n type user name and ids again or type quit: ')
        if terminate == 'quit':
            active = False
    for username, ids in credentials.items():
        print(f'{username} => {ids}')
        return credentials


if __name__ == '__main__':
    import sys
    main(sys.argv)
