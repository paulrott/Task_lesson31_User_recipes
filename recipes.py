class Recipe:

    number_of_cooking_stages = 3

    def __init__(self,name,ingredients,annotation,cooking_time,cooking_device):
        self.name = name
        self.ingredients = ingredients
        self.annotation = annotation
        self.cooking_time = cooking_time
        self.cooking_device = cooking_device
    def public_recipe(self):
        print("\033[31m {}" .format(self.name))
        print("\033[31m {}" .format(self.ingredients))
        print("\033[31m {}" .format(self.annotation))
        print("\033[31m {}" .format(self.cooking_time))
        print("\033[31m {}" .format(self.cooking_device))



recipe_1 = Recipe(name='Chicken soup', ingredients='potato,chiken breast,salt,carrot,onion', annotation = 'vegetable soup with chicken breast',cooking_time = '40',cooking_device =
'RMC-M903S')
recipe_1.public_recipe()


# print(recipe_1.name)
# print(recipe_1.ingredients)
# print(recipe_1.annotation)
# print(recipe_1.cooking_time)
# print(recipe_1.cooking_device)



recipe_2 = Recipe(name='hot dog', ingredients='sausage,bun,ketchup,mayonnaise', annotation = 'wheat bun with sausage seasoned with ketchup, mayonnaise, mustard',cooking_time = '10',cooking_device =
'none')

print(("\033[35m {}" .format(recipe_2.name)))
print(("\033[35m {}" .format(recipe_2.ingredients)))
print(("\033[35m {}" .format(recipe_2.annotation)))
print(("\033[35m {}" .format(recipe_2.cooking_time)))
print(("\033[35m {}" .format(recipe_2.cooking_device)))



recipe_3 = Recipe(name='омлет', ingredients='milk,eggs,milk', annotation = 'нежный омлет с молоком',cooking_time = '20',cooking_device = 'SkyBaker')


print(("\033[34m {}" .format(recipe_3.name)))
print(("\033[34m {}" .format(recipe_3.ingredients)))
print(("\033[34m {}" .format(recipe_3.annotation)))
print(("\033[34m {}" .format(recipe_3.cooking_time)))
print(("\033[34m {}" .format(recipe_3.cooking_device)))