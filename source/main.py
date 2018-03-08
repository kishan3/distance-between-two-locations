import os

from distance_calculator import calculate_distance

dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    file_path = dir_path + "/customers.txt"
    calculate_distance(file_path=file_path)
