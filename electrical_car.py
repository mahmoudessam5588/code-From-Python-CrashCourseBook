from Car_class import Car

class Electical_Car(Car):
 def __init__(self, make, model, year):
    super().__init__(make, model, year)
    self.battery_size = None
 def describe_battery(self,battery):
    self.battery_size= battery 
    print('the battery size has :'+ str(battery) + 'KWH ')
    return battery
 def fill_gas_tank():
    print("This car doesn't need a gas tank!")  
 def get_range(self,message):
  self.battery_size = message
  range = 0   
  if message == 70:
    range = 240
  elif message == 85:
    range = 270
  message = "This car can go approximately " + str(range)
  message += " miles on a full charge."
  print(message)
  return message      