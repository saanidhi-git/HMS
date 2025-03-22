from data import *
class Menu:
    def __init__(self,maincourse,beverages):
        self.maincourse=maincourse
        self.beverages=beverages
        self.menu_print()
    def menu_print(self):
       food_categories = [maincourse,beverages]
       for category in food_categories:
           for food,price in category.items() :
               print(f"{food}:{price}Rs")