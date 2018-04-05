import pytest
from DishClasses import *


def test_DrinkName_with_space_positive():
	new_dish = MyDish('Fried Popatoes',0,100)
	new_dish.print_dish()
	assert new_dish.name == 'Fried Popatoes'
	
def test_time_for_cooking_is_negative():
	new_dish = MyDish('Cucumber',-5,100)
	new_dish.print_dish()
	assert NameError, 'Time cannot be negative!'