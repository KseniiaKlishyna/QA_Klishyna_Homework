from Homework_14.Homework_14 import CSVOperations
import csv


class TestCSVOperations:
    @classmethod
    def setup_class(cls):
        print("it's setup class")

    def setup(self):
        self.file = CSVOperations('new_csv.csv')
        print('setup for each test')

    def test_add_line(self):
        file = self.file

        with open(self.file.filename, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            all_lines = list(csv_reader)

        new_line = ["New,new line"]
        file.add_line(new_line)

        with open(self.file.filename, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            lines = list(csv_reader)

        assert len(lines) == len(all_lines) + 1
        assert lines[-1] == new_line

    def test_remove_line(self):
        file = self.file

        with open(self.file.filename, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            all_lines = list(csv_reader)

        index_to_remove = 0
        file.remove_line(index_to_remove)

        with open(self.file.filename, 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            lines = list(csv_reader)

        assert len(lines) == len(all_lines) - 1
        assert lines[index_to_remove] != all_lines[index_to_remove]

    @staticmethod
    def teardown():
        print('teardown for each test')

    @staticmethod
    def teardown_class():
        print('it`s teardown class')
