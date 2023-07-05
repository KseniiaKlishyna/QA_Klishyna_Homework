key_word = input("Список команд: \n add - додати нотатку"+
            " \n earliest - виводить збережені нотатки від найстарішої до найновішої" +
            " \n latest - виводить збережені нотатки від найновішої до найстарішої"+
            " \n longest - виводить збережені нотатки від найдовшої до найкоротшої"
            " \n shortest - виводить збережені нотатки від найкоротшої до найдовшої"
            " \n exit - вихід \n Введіть команду: ")

key_word = key_word.lower() # преобразовываем все символы в нижний регистр
key_word = key_word.strip() # убираем пробелы
notes = []

while True:
    if key_word == "add": # добавляем нотатку
        new_note = input("Введіть нотатку: ")
        notes.append(new_note)
        key_word = input("Введіть команду: ")
        key_word = key_word.lower()
        key_word = key_word.strip()
        continue
    elif key_word == 'earliest': #Выводим список как он есть ( от старого к новому)
        print(notes)
        key_word = input("Введіть команду: ")
        key_word = key_word.lower()
        key_word = key_word.strip()
        continue
    elif key_word == 'latest': #Переворачиваем список
        print(list(reversed(notes)))
        key_word = input("Введіть команду: ")
        key_word = key_word.lower()
        key_word = key_word.strip()
        continue
    elif key_word == "longest": #сортируем по длине и переворачиваем
        longest_notes = sorted(notes, key=len, reverse=True)
        print(longest_notes)
        key_word = input("Введіть команду: ")
        key_word = key_word.lower()
        key_word = key_word.strip()
        continue
    elif key_word == "shortest": #сортируем по ключу длина ( по умолчанию сортировка от самого короткого)
        shortest_notes = sorted(notes, key=len)
        print(shortest_notes)
        key_word = input("Введіть команду: ")
        key_word = key_word.lower()
        key_word = key_word.strip()
        continue
    elif key_word == 'exit':
        print("До зустрічі!")
        break
    else:
        key_word = input("Будь ласка введіть команду зі списку. \nВведіть команду: ")
        key_word = key_word.lower()
        key_word = key_word.strip()
        continue

