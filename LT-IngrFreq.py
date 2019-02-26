


import json
import csv

'''import dataset (copied from Justin's code)'''

file = open('test_ingr.json','r')   #make sure this flle is in the same directory as the notebook file
#with open('det_ingrs.json','r') as file:
data = json.load(file)







'''count frequency of each ingredient'''

print(len(data))
# print('data[0]:', data[0])

ingr_raw = []  # keeps track of all ingredients in all recipes
for x in data[:2000]:
    for i in range(len(x['ingredients'])):
            if x['valid'][i]:
                ingr_raw.append(x['ingredients'][i]['text'])

food_dict = {} # key: ingredient name;  value: count of occurences
for i in ingr_raw:
    if i not in food_dict:
        food_dict[i] = 1
    else:
        food_dict[i] += 1
# print(food_dict)

food_dict_sorted = sorted(food_dict.items(), key = lambda kv: kv[1])
print(food_dict_sorted)


# sorts dictionary by values (occurences)
