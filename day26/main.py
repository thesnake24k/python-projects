import random
# list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7]
new_number = [n * 2 for n in numbers]
print(new_number)
name = "Oussama"
list_name = [letter for letter in name]
print(list_name)

double_range = [r * 2 for r in range(1, 5)]
print(double_range)
names = ["Oussama", "Yurika", "Amira", "Baka"]
new_names = [nam.upper() for nam in names if len(nam) > 4]
print(new_names)

# dictionary comprehension

names = ["Oussama", "Yurika", "Amira", "Baka", "dodo", "bobo", "soso", "jojo"]
name_dict = {nam: random.randint(0, 100) for nam in names}
print(name_dict)
passed_names = {nom: score for (nom, score) in name_dict.items() if score >= 60}
print(passed_names)
