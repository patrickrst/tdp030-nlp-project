import sys
import ast
import collections

def open_dataset():
    dataset = sys.argv[1]
    print(sys.argv[1])
    open_dataset = open(dataset, "r")
    lines = []
    recipes = []
    i = 0
    for line in open_dataset:
        if i == 0 or i == 1029721:
            pass
        else:
            recipes.append(ast.literal_eval(line))
        i += 1
    return recipes

def main():
    recipes = open_dataset()
    recipe_n = ""
    keyword = ""
    print("recipe_n:", "0 -", str(len(recipes)))
    print("Keywords: ")
    print("     ingredients")
    print("     title")
    print("     instructions")
    print("     url")
    print("     id")
    while recipe_n != "quit" or keyword != "quit":
        recipe_n = input("Enter recipe_n: ")
        keyword = input("Enter word: ")
        try:
            print(str(keyword) + ": ", str(recipes[int(recipe_n)][0][keyword]))
        except:
            print("Something went wrong, did you type in the correct recipe_n and keyword?")
        print("")

if __name__ == "__main__":
    main()
