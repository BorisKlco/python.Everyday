import pandas

data = pandas.read_csv("nafo.csv")

nafo = {code["letter"]:code["code"] for (index,code) in data.iterrows()}

user_input = input("\nword: ")

output = [nafo[char.upper()] for char in user_input if char.isalpha()]

print(output)