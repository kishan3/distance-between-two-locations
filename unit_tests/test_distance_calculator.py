import os
import unittest

from source.constants import BASE_LONGITUDE, BASE_LATITUDE
from source.distance_calculator import degree_to_radians, get_distance_in_kilometers, calculate_distance

dir_path = os.path.dirname(os.path.realpath(__file__))


class TestFileOperations(unittest.TestCase):
    def test_degree_to_radians(self):
        assert degree_to_radians(53.339428) == 0.9309486397304539
        assert degree_to_radians(0) == 0.0
        assert degree_to_radians(90) == 1.5707963267948966

    def test_degree_to_radians_invalid(self):
        self.assertRaises(TypeError, lambda: degree_to_radians("hello"))
        self.assertRaises(TypeError, lambda: degree_to_radians("102.25"))

    def test_get_distance_in_kilometers_valid(self):
        distance = get_distance_in_kilometers(latitude_degree1=52.986375,
                                              longitude_degree1=-6.043701,
                                              latidude_degree2=BASE_LATITUDE,
                                              longitude_degree2=BASE_LONGITUDE)
        assert distance == 41.7687255008362

        distance = get_distance_in_kilometers(latitude_degree1=0,
                                              longitude_degree1=0,
                                              latidude_degree2=BASE_LATITUDE,
                                              longitude_degree2=BASE_LONGITUDE)
        assert distance == 5959.281223177746

    def test_get_distance_in_kilometers_invalid(self):
        self.assertRaises(TypeError, lambda: get_distance_in_kilometers(latitude_degree1="52.986375",
                                                                        longitude_degree1="-6.043701",
                                                                        latidude_degree2=BASE_LATITUDE,
                                                                        longitude_degree2=BASE_LONGITUDE))

        self.assertRaises(TypeError, lambda: get_distance_in_kilometers(latitude_degree1=[0],
                                                                        longitude_degree1=[0],
                                                                        latidude_degree2=BASE_LATITUDE,
                                                                        longitude_degree2=BASE_LONGITUDE))

    def test_calculate_distance(self):
        assert type(calculate_distance(dir_path + "/dummy_data/ideal_customer_data.txt")) == list
        # Emtpy list/dicts evaluates to False so we check using it.
        self.assertTrue(calculate_distance(dir_path + "/dummy_data/ideal_customer_data.txt"))
        self.assertTrue(calculate_distance(dir_path + "/dummy_data/corrupt_customer_data.txt"))
        self.assertFalse(calculate_distance(dir_path + "/dummy_data/empty_file.txt"))
