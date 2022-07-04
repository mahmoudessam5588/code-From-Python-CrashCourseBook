import crash_course
def full_name_profile(first,last,**user_profile):
    profile={}
    profile['firstName'] = first
    profile['lastName'] = last
    for key,value in user_profile.items():
        profile[key]=value
    return profile
full_name_profile('mahmoud','essam')
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Sit(self):
        print(f'{self.name.title()} is now sitting ')
    def Roll_Over(self):
        print(f'{self.name.title()} rolled over ')        