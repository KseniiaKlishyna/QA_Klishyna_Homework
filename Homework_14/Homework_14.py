import csv
import json

# Напишіть адаптер, який конвертує json в csv


class JSONConverter:
    def __init__(self):
        self.__lines = []

    def read_file(self, filename: str):
        with open(filename, 'r') as json_file:
            self.__data = json.load(json_file)

    def write_file(self, filename: str):
        if not self.__lines:
            return

        fieldnames = self.__lines[0].keys()

        with open(filename, 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            csv_writer.writerows(self.__data)

    def cleanup(self):
        self.__lines = []


converter = JSONConverter()
converter.read_file('example.json')
converter.write_file('example.csv')

# 2 завдання. скористайтесь pytest. напишіть функцію, яка додає в csv один рядок. Напишіть функцію, яка видаляє з csv один рядок.
# напишіть два тести, які перевіряють відповідно чи додався рядок і чи він видалився. в якості перевірного csv можете скористатись доданим до завдання файлом або будь-яким іншим.


class CSVOperations:
    def __init__(self, filename):
        self.filename = filename

    def add_line(self, data):
        with open(self.filename, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)

    def remove_line(self, index):
        lines = []
        with open(self.filename, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                lines.append(row)

        try:
            index = int(index)  # Convert the index to an integer
            if 0 <= index < len(lines):
                del lines[index]
        except ValueError:
            pass  # Handle the case where index is not a valid integer

        with open(self.filename, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(lines)
