import os
import sys


class CreateNewDay:

    def __init__(self, day_number: int):
        self.directory = "../AdventofCode2021/Day%s" % day_number
        self.data_file_path = self.directory + "/Day%sData.txt" % day_number
        self.small_data_file_path = self.directory + "/Day%sSmallData.txt" % day_number
        self.python_file_path = self.directory + "/Day%s.py" % day_number

        os.mkdir(self.directory)
        self.make_data_file()
        self.make_python_file(day_number)

    def make_data_file(self) -> None:
        new_data_file = open(self.data_file_path, "w")
        new_data_file.close()

        new_small_data_file = open(self.small_data_file_path, "w")
        new_small_data_file.close()

    def make_python_file(self, day_number: int) -> None:
        new_python_file = open(self.python_file_path, "w")
        python_file_template = open("DayCreation/DayTemplate.txt", "r")

        for line in python_file_template:
            new_python_file.write(line.replace("{DayNumber}", str(day_number)))

        new_python_file.close()
        python_file_template.close()


if __name__ == "__main__":
    day_number = int(sys.argv[1])
    CreateNewDay(day_number)
