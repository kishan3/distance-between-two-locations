import json


def read_customer_data(file_path):
    """
    Open file and read file data. If any line is corrupt or not in
    proper json format we ignore that data and continue to reading next line.

    Arguments:
    file_path
    Return:
    A list of customer data from file.
    """
    customer_data = []
    try:
        file_object = open(file_path, "rb")
        for line in file_object.readlines():
            try:
                customer_data.append(json.loads(line.strip()))
            except ValueError as e:
                print(e.message)
                continue
        file_object.close()
    except IOError as e:
        print(e.message)
    return customer_data
