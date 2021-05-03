
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

# print(food[0])

food.append("ice scream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
# food.clear()

for x in food:
    print(x)