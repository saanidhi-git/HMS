class Menu:
    def __init__(self, maincourse, beverages):
        self.maincourse = maincourse
        self.beverages = beverages
        self.menu_print()

    def menu_print(self):
        # Use self.maincourse and self.beverages
        food_categories = [self.maincourse, self.beverages]
        for category in food_categories:
            for food, price in category.items():
                print(f"{food}: {price}Rs")


# Create an instance of the Menu class
if __name__ == "__main__":
    menu = Menu(maincourse, beverages)