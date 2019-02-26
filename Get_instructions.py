import json
import csv
import Ingr_frek


def main():
    list_of_ingredients = Ingr_frek.main()
    unique_ingredients = list_of_ingredients[1]
    frequency_of_ingredients = list_of_ingredients[0]
    file = open('layer1.json','r')   #make sure this flle is in the same directory as the notebook file
    data = json.load(file)

    chosen_ingredient = "Chinese cabbage"

    if chosen_ingredient in "Put Chinese cabbage in fridge":
        print("hi")
    for recipe in data:
        ingredient_in_recipe = False
        for ingredient in recipe["ingredients"]:
            if chosen_ingredient in ingredient["text"]:
                ingredient_in_recipe = True
        if ingredient_in_recipe:
            for sentence in recipe["instructions"]:
                if chosen_ingredient in sentence["text"]:
                    print(sentence["text"])
    #print(unique_ingredients)



main()
