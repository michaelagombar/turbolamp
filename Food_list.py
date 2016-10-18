def add_food(food_list, food_category):
    current_food = " "
    while current_food != "":
        current_food = input('What kind of ' + food_category + ' do you want?')
        if current_food in food_list:
            print("You already have this item!")
            food_list.remove(current_food)
        elif current_food !="":
            current_food = input('What kind of ' + food_category + ' do you want?')
            food_list.append(current_food)
            print("You need to buy: " + food_list)




snacks = ["granola bars", "chips", "easy mac"]
vegetables = ["onions", "tomatoes", "asparagus", "corn", "peppers", "mushrooms"]
meat = ["chicken", "brats", "steak", "ground beef"]

add_food(snacks, 'snacks')
add_food(vegetables, 'vegetabales')
add_food(meat, 'meat')
