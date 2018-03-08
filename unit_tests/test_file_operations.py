import os
import unittest

from source.file_operations import read_customer_data

dir_path = os.path.dirname(os.path.realpath(__file__))


class TestFileOperations(unittest.TestCase):

    def test_read_customer_data_file_exists(self):
        data = read_customer_data(dir_path + "/dummy_data/ideal_customer_data.txt")
        assert type(data) is list

    def test_read_customer_data_file_donot_exist(self):
        data = read_customer_data(dir_path + "/dummy_data/non_existing_file.txt")
        assert type(data) == list
        assert len(data) == 0

    def test_read_customer_data_empty_file(self):
        data = read_customer_data(dir_path + "/dummy_data/empty_file.txt")
        assert type(data) == list
        assert len(data) == 0

    def test_read_customer_data_corrupt_data(self):
        data = read_customer_data(dir_path + "/dummy_data/corrupt_customer_data.txt")
        assert type(data) == list
