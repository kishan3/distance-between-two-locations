from math import radians, sin, cos, sqrt, asin
from operator import itemgetter

from constants import INVITATION_THRESHOLD, BASE_LATITUDE, BASE_LONGITUDE
from file_operations import read_customer_data


def degree_to_radians(degree):
    """
    Convert degree into radians.
    :param degree: degree to be converted (float or int)
    :return: radians equivalent of degree given
    """
    return radians(degree)


def get_distance_in_kilometers(latitude_degree1, longitude_degree1, latidude_degree2, longitude_degree2):
    """
    Calculate distance between two points using haversine formula.

    :param latitude_degree1:
    :param longitude_degree1:
    :param latidude_degree2:
    :param longitude_degree2:
    :return: Distance in kilometers
    """
    R = 6371  # Radius of the earth in km
    delta_latidude = degree_to_radians(latidude_degree2 - latitude_degree1)
    delta_longitude = degree_to_radians(longitude_degree2 - longitude_degree1)
    latidude_radian1 = degree_to_radians(latitude_degree1)
    latidude_radian2 = degree_to_radians(latidude_degree2)

    a = sin(delta_latidude / 2) ** 2 + \
        cos(latidude_radian1) * cos(latidude_radian2) * sin(delta_longitude / 2) ** 2

    c = 2 * asin(sqrt(a))
    distance = R * c  # Distance in km
    return distance


def calculate_distance(file_path):
    """
    Read file data and process.

    :param file_path: Path of the file to begin with.
    :return: Customers to be invited sorted by their user id.
    """
    customer_data = read_customer_data(file_path=file_path)
    customers_tobe_invited = []
    for customer in customer_data:
        distance = get_distance_in_kilometers(latitude_degree1=float(customer["latitude"]),
                                              longitude_degree1=float(customer["longitude"]),
                                              latidude_degree2=BASE_LATITUDE,
                                              longitude_degree2=BASE_LONGITUDE)
        if distance <= INVITATION_THRESHOLD:
            customer.update({"distance": distance})
            customers_tobe_invited.append(customer)
        customers_tobe_invited = sorted(customers_tobe_invited, key=itemgetter('user_id'))

    for invited_customer in customers_tobe_invited:
        print "Distance for customer User id {} - Name {}: {}".format(invited_customer["user_id"],
                                                                      invited_customer["name"],
                                                                      invited_customer["distance"])
    return customers_tobe_invited
