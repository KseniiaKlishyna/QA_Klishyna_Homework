import random
#Task 1
def sorted_list(list_1, list_2):
    new_list = list(set(list_1) & set(list_2))
    return sorted(new_list)

list_1 = [1, 0,  0.3, 567, 339,  222]
list_2 = [4859, 5, 0, -94, 339]

print(sorted_list(list_1, list_2))

# Task 2
def average_score(students):
    for val in students.items():
        val = students.values()
        average_val = int(sum(val)/ len(val))
        return average_val

def best_students_list(students): # list with best students
    students_dict = {}
    for key, val in students.items():
        if val > average_score(students):
            students_dict[key] = val
    return list(students_dict)

class_scores = {"Alex": 78, "Lois":68, "Adam": 59, "Ami":34, "Barbara":89, "Den":100, "Dil": 48}

print(best_students_list(class_scores))

#Task 3
def random_dict(key1, key2, key3):
    new_dictionary = {}
    for i in range (0,2):
        a = random.randint(0, 3)
        b = random.randint(0, 2)
        c = random.randint(0, 2)
    new_dictionary = {"name":key1[a],"surname":key2[b], "location":key3[c]}
    return new_dictionary

name = ["Anna", "John", "Jack", "Chloe"]
surname = ["Braun", "Robinson", "Sparrow"]
location = ["Europe", "USA", "Africa"]

print(random_dict(name,surname,location))
