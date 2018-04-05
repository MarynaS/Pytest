import random

dishes_string = ('eggs, Cake, cake, Spam, Spam   ,,, Butter, New, new, cookie, water , juice')
drink_string = ["Water","Juice","Sprite","Coffee"]

new_list =[]
dish_set = []

class MyServing():
    def __init__(self, name,random_a,random_b):
        if (random_a < 0) and (random_b <0):
        	raise NameError('Time cannot be negative!')
        self.name = name
        self.random_a = random_a
        self.random_b = random_b
 
    def call_time(self):
        dish_time = random.randint(self.random_a,self.random_b)
        return (dish_time)

    def print_dish(self):
        print ("{:.<15}{:.>20} min"
        .format(self.name,self.call_time()))

class MyDish(MyServing):
    pass

class MyDrink(MyServing):
    def __init__(self,name, random_a, random_b):
        MyServing.__init__(self,name,random_a,random_b)

    def print_drink(self):
        print ("{:.<15}{:.>20} min"
        .format(self.name,self.call_time()))
        
for el in dishes_string.title().split(','):
    if el.strip() != "":
        new_list.append(el.strip())
        dish_ordered = list(set(new_list))

for dish in dish_ordered:
    if (dish in drink_string):
        time_for_drink = MyDrink(dish,5,5)
        time_for_drink.print_drink()
    else:
        time_for_dish = MyDish(dish,0,100)
        time_for_dish.print_dish()        