import csv
# 1 Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів
# (domains.txt) та повертає їх у вигляді списку рядків (назви повертати без крапки).

with open('domains.txt', 'r') as file_1:
    list_1 = [line.strip() for line in file_1]
    list_1 = [i.replace(".","") for i in list_1]
    print(list_1)

# 2 Написати функцію, яка отримує у вигляді параметра ім'я файлу (names.txt) і повертає список усіх прізвищ з нього.
# Кожен рядок файлу містить номер, прізвище, країну. Файл створити власноруч і записати туди дані

with open('names.txt') as file_2:
    dict_names= csv.reader(file_2, delimiter=',')
    for row in dict_names:
        print(row[1])
# 3 Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) і
# повертає список словників виду { "date": date, у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
def list_of_dict(x):
    new_dict = {}
    for i in x:
        if i == 'January':
            new_dict["date"] = x[i]
        else:
            new_dict[i] = x[i]
            del new_dict[i]
    return (new_dict)

list_3 = []
with open('authors.txt') as file_3:
    dict_1 = csv.DictReader(file_3, delimiter='-')
    for line in dict_1:
        list_3.append(list_of_dict(line))
    print(list_3)










